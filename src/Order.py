'''
Created on 2014-01-09

@author: julienbacon
'''

from collections import deque
from datetime import date
from ProductOrder import ProductOrder
import os
from xlrd import open_workbook, XL_CELL_EMPTY, XL_CELL_TEXT, XL_CELL_NUMBER
import xlutils
from xlwt import Workbook

class OrderError(Exception):
    '''
    Base exception for Order
    '''

class Order:
    '''
    Order is a list of ProductOrders.
    It creates its list from an excel file. If the file was not modify earlier
    than yesterday, Order assumes that there's nothing new to order.
    
    It give the following interaces:
        - Load the ProductOrder from an excel file in read only or read/write mode.
        - Append one ProductOrder.
        - Get the ProductOrder list.
        - Get one ProductOrder.
    '''
    __DAILY_ORDER_SH_NAME = 'dailyOrder'
    __ORDERED_SH_NAME = 'ordere'
    __TITLE_ROW = 0
    __1ST_DATA_ROW = 1
    __LAST_DATA_ROW = 13
    __PROD_NB_TITLE = 'no. produit'
    __DESC_TITLE = 'description'
    __QTY_TITLE = 'quantite'
    __DATE_TILE = 'date'
    __EMPLOYEE_TITLE = 'commis'
    __TITLE_MAP = (__PROD_NB_TITLE, __DESC_TITLE, __QTY_TITLE, __DATE_TILE,
                   __EMPLOYEE_TITLE)
    __ADMIN_EMPLOYEE = 'jf admin'
    
    def __colMapping(self, sheet):
        #parse the col. to figure which one has what data
        tempList = list()
        for col in range(sheet.ncols):
            for title in self.__TITLE_MAP:
                if sheet.cell(self.__TITLE_ROW, col).value == title:
                    tempList.append(col)
                    if title == self.__EMPLOYEE_TITLE:
                        self.__colMap.append(tempList)
                        tempList = list()
    
    def __rowMapping(self, sheet):
        flagedAsData = False
        #for each order bloc
        for orderBloc in self.__colMap:
            #parse the row to figure which one containt data (partial or complete)
            tempList = list()
            for row in range(self.__1ST_DATA_ROW, self.__LAST_DATA_ROW + 1):
                for col in orderBloc:
                    if sheet.cell(row, col).value:
                        flagedAsData = True
                if flagedAsData:
                    tempList.append(row)
                    flagedAsData = False
            self.__rowMap.append(tempList)
            tempList = list()
    
    def __processLoading(self, sheet, withDateFlag):
        #for each order bloc, load the data
        for orderBloc in self.__colMap:
            #if there's a date in the file, construct the order list with the
            #date from the file
            currentDate = date.today()
            for row in self.__rowMap.popleft():
                prodOrder = ProductOrder()
                if withDateFlag:
                    (prodNbCol, qtyCol, descCol, dateCol, employeeCol) = orderBloc
                    if sheet.cell(row, dateCol).ctype == XL_CELL_TEXT:
                        try:
                            prodOrder[ProductOrder.DATE_KEY] = \
                                str(sheet.cell(row, dateCol).value)
                        except:
                            #put in the log file
                            pass
                else:
                    (prodNbCol, qtyCol, descCol, employeeCol) = orderBloc
                    prodOrder[ProductOrder.DATE_KEY] = currentDate
                if sheet.cell(row, prodNbCol).ctype == XL_CELL_NUMBER:
                    prodOrder[ProductOrder.PROD_NB_KEY] = \
                        int(sheet.cell(row, prodNbCol).value)
                if sheet.cell(row, qtyCol).ctype == XL_CELL_NUMBER:
                    prodOrder[ProductOrder.QTY_TO_ORDER_KEY] = \
                        int(sheet.cell(row, qtyCol).value)
                if sheet.cell(row, descCol).ctype == XL_CELL_TEXT:
                    prodOrder[ProductOrder.DESC_KEY] = \
                        str(sheet.cell(row, descCol).value)
                if sheet.cell(row, employeeCol).ctype == XL_CELL_TEXT:
                    prodOrder[ProductOrder.EMPLOYEE_KEY] = \
                        str(sheet.cell(row, employeeCol).value)
                self.__oderList.append(prodOrder)
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__oderList = deque()
        self.__colMap = []
        self.__rowMap = deque()
        
    def __len__(self):
        '''
        Get the length of the actual ProductOrder list.
        '''
        return len(self.__oderList)
        
    def loadOrder(self, sourceFile, withDateFlag = False):
        '''
        Load an Order in read only mode.
        '''
        try:
            book = open_workbook(sourceFile, on_demand = True)
        except:
            pass
        sheet = book.sheet_by_index(0)
        #figure if there's something new to order
        if sheet.nrows == 1:
            pass #raise exception
        #build the map of the data
        self.__colMapping(sheet)
        self.__rowMapping(sheet)
        #process the data
        self.__processLoading(sheet, withDateFlag)
        book.release_resources()
        
    def append(self, prodOrder):
        '''
        Append a ProductOrder
        '''
        self.__oderList.append(prodOrder)
        
    def popLeft(self):
        '''
        Pop left the ProductOrder list.
        '''
        return self.__oderList.popleft()
    
    def popRight(self):
        '''
        Pop right th ProductOrder list.
        '''
        return self.__oderList.pop()
    
    def filter(self, ordered):
        '''
        Filter bad and already ordered ProductOrder.
        Filters are:
            - bad ProductOrder.
            - Already Ordered in the last 20 days ProductOrder, except if employee is the admin.
        '''
        filteredProdOrder = list()
        #filter the bad productOrder
        for prodOrder in self.__oderList:
            if not prodOrder.isValid():
                filteredProdOrder.append(prodOrder)
        #remove the ProductOrder filtered
        for prodOrder in filteredProdOrder:
            self.__oderList.remove(prodOrder)
        #filter already ordered
        filteredProdOrder = list()
        for prodOrder in self.__oderList:
            for oldOrder in ordered.getOrderList():
                if prodOrder == oldOrder and \
                        -20 < prodOrder.deltaProductOrder(oldOrder) < 20 and \
                        prodOrder[ProductOrder.EMPLOYEE_KEY] != self.__ADMIN_EMPLOYEE:
                    filteredProdOrder.append(prodOrder)
        #remove the ProductOrder filtered
        for prodOrder in filteredProdOrder:
            self.__oderList.remove(prodOrder)
            
    def getOrderList(self):
        '''
        Get the whole ProductOrder list.
        '''
        return self.__oderList
    
    def clear(self):
        '''
        Clear the order
        '''
        self.__oderList.clear()
    
    def save(self, destinationFile):
        '''
        Save the order data to the destination file
        '''
        