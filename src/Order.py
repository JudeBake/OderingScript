'''
Created on 2014-01-09

@author: julienbacon
'''

from ProductOrder import ProductOrder
import os
from xlrd import open_workbook
from xlwt import Workbook

class OrderError(Exception):
    '''
    Base exception for Order
    '''

class Order:
    '''
    Order is a wrapper of a list of ProductOrders.
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
    __PROD_NB_TITLE = 'Produt Number'
    __DESC_TITLE = 'Description'
    __QTY_TITLE = 'Quantity'
    __DATE_TILE = 'Date'
    
    def __colMappingBuilder(self, sheet):
        colMapping = {self.__PROD_NB_TITLE:list(), self.__DESC_TITLE:list(),
                      self.__QTY_TITLE:list(), self.__DATE_TILE:list()}
        for col in range(sheet.ncols):
            for title in colMapping.keys():
                if sheet.cell(self.__TITLE_ROW, col).value == title:
                    colMapping[title].append(col)
        return colMapping
    
    def __processOrder(self, sheet):
        for row in range(self.__1ST_DATA_ROW, sheet.nrows):
            for col in (self.__PROD_NB_COL, self.__DESC_COL, self.__QTY_COL,
                        self.__DATE_COL):
                value = sheet.cell(row, col).value
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__oderList = []
        
    def loadOrder(self, sourceFile):
        '''
        Load an Order in read only mode.
        '''
        try:
            book = open_workbook(sourceFile, on_demand = True)
        except:
            pass
        sheet = book.sheet_by_name(self.__DAILY_ORDER_SH_NAME)
        #figure if there's something new to order
        if sheet.nrows == 1:
            pass #raise exception
        self.__processOrder(sheet)
  
        
    def getOrderList(self):
        '''
        Get the ProductOrderList.
        '''
        return self.__oderList
        