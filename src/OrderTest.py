'''
Created on 2014-01-09

@author: julienbacon
'''

from datetime import date
from Log import Log
from ProductOrder import ProductOrder
from Order import Order, sourceFileDontExist, emptyOrder
import os
import unittest

TEST_FILE_ROOT = r'..\test_files'

def productOrderBuilder(prodNb, desc, qty, date, employee):
    prodOrder = ProductOrder()
    prodOrder[ProductOrder.PROD_NB_KEY] = prodNb
    prodOrder[ProductOrder.DESC_KEY] = desc
    prodOrder[ProductOrder.QTY_TO_ORDER_KEY] = qty
    prodOrder[ProductOrder.DATE_KEY] = date
    prodOrder[ProductOrder.EMPLOYEE_KEY] = employee
    return prodOrder
    
class OrderLoadingTest(unittest.TestCase):
    ATTENDED_RESULTS = [productOrderBuilder('', '', 200, date(1232, 4, 13), ''),
                         productOrderBuilder('130050', 'coucou', None, date(1231, 4, 13), 'Daniel'),
                         productOrderBuilder('133840', 'dodo', 50, date(2001, 1, 1), 'justin'),
                         productOrderBuilder('130090', '', None, None, ''),
                         productOrderBuilder('203432', 'bonjour', 2000, date(2001, 1, 1), 'jf'),
                         productOrderBuilder('133045', 'allo', 100, date(2001, 1, 1), 'jb')]
        
    def testOrderLoading(self):
        '''
        Order must be able to load its ProductOrders from an excel file, get its
        length and pop right its whole ProductOrder list.
        '''
        log = Log()
        order = Order(log)
        order.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile1.xls'))
        result = []
        for i in range(len(order)):
            result.append(order.popRight())
        i = i
        self.assertListEqual(result, self.ATTENDED_RESULTS, 'Order failed to load its ProductOrder list from an excel file, get its length and popRight its whole ProductOrder list')
        
    def testNoOrderFile(self):
        '''
        Order must raise sourceFileDontExist error when trying load an order
        from an non-existent file.
        '''
        log = Log()
        order = Order(log)
        self.assertRaises(sourceFileDontExist, order.loadOrder,
                          os.path.join(TEST_FILE_ROOT, 'allo.xls'))
        
    def testEmptyOrder(self):
        '''
        Order must raise an emptyOrder exception when trying to load an empty
        order file.
        '''
        log = Log()
        order = Order(log)
        self.assertRaises(emptyOrder, order.loadOrder,
                          os.path.join(TEST_FILE_ROOT, 'OrderTestFile8.xls'))
        
class filterOderTest(unittest.TestCase):
    ATTENDED_RESULTS = [productOrderBuilder('203432', 'bonjour', 2000, date(2014, 1, 14), 'jf admin'),
                        productOrderBuilder('240900', 'lala', 100, date(2014, 1, 14), 'guy'),
                        productOrderBuilder('130090', 'prout', 200, date(2014, 1, 14), 'jb'),
                        productOrderBuilder('133840', 'dodo', 50, date(2014, 1, 14), 'justin')]
    
    def testFilterOrder(self):
        '''
        Order must be able to filter and remove the bad ProductOrder and those
        already ordered.
        The filters are:
            - imcomplete or incoherent ProductOrder.
            - Already ordered in the last 20 days ProductOrder, except if employee is the admin.
        '''
        log =Log()
        order1 = Order(log)
        order2 = Order(log)
        order1.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile2.xls'))
        order2.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile3.xls'))
        order1.filter(order2)
        result = []
        for i in range(len(order1)):
            result.append(order1.popLeft())
        i = i
        self.assertListEqual(result, self.ATTENDED_RESULTS, 'Order failed to filter and remove the bad and already ordered ProductOrder.')
        
class clearAndSaveTest (unittest.TestCase):
    
    def setUp(self):
        '''
        Setup the test case by loading the contant of the files to process the
        attended result.
        '''
        self.__log = Log()
        self.__originalFile1 = Order(self.__log)
        self.__originalFile2 = Order(self.__log)
        self.__originalFile1.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile4.xls'))
        self.__originalFile2.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile5.xls'))
        self.__attendedResult2 = []
        for prodOrder in self.__originalFile1.getOrderList():
            self.__originalFile2.append(prodOrder)
        for prodOrder in self.__originalFile2.getOrderList():
            self.__attendedResult2.append(prodOrder)
            
    def tearDown(self):
        '''
        Deleted the new files.
        '''
        os.remove(os.path.join(TEST_FILE_ROOT, 'OrderTestFile6.xls'))
        os.remove(os.path.join(TEST_FILE_ROOT, 'OrderTestFile7.xls'))
        
    def testClearAndSave(self):
        '''
        Order must be able to clear and save itself.
        '''
        order1 = Order(self.__log)
        order2 = Order(self.__log)
        order1.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile4.xls'))
        order2.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile5.xls'))
        for i in range(len(order1)):
            order2.append(order1.popLeft())
        i = i
        order1.clear()
        order1.save(os.path.join(TEST_FILE_ROOT, 'OrderTestFile6.xls'))
        order2.save(os.path.join(TEST_FILE_ROOT, 'OrderTestFile7.xls'))
        resultOrder1 = Order(self.__log)
        resultOrder2 = Order(self.__log)
        try:
            resultOrder1.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile6.xls'))
        except:
            pass
        resultOrder2.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile7.xls'))
        result1 = []
        result2 = []
        for prodOrder in resultOrder1.getOrderList():
            result1.append(prodOrder)
        for prodOrder in resultOrder2.getOrderList():
            result2.append(prodOrder)
        self.assertListEqual(result1, [], 'Order failed to clear itself.')
        self.assertListEqual(result2, self.__attendedResult2, 'Order failed to save itself.')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()