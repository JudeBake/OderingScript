'''
Created on 2014-01-09

@author: julienbacon
'''

from datetime import date
from ProductOrder import ProductOrder
from Order import Order
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
    ATTENDED_RESULTS1 = [productOrderBuilder(133045, 'allo', 100, date.today(), 'jb'),
                         productOrderBuilder(203432, 'bonjour', 2000, date.today(), 'jf'),
                         productOrderBuilder(130090, '', None, date.today(), ''),
                         productOrderBuilder(133840, 'dodo', 50, date.today(), 'justin'),
                         productOrderBuilder(130050, 'coucou', None, date.today(), 'Daniel'),
                         productOrderBuilder(None, '', 200, date.today(), '')]
    ATTENDED_RESULTS2 = [productOrderBuilder(None, '', 200, date(1232, 4, 13), ''),
                         productOrderBuilder(130050, 'coucou', None, date(1231, 4, 13), 'Daniel'),
                         productOrderBuilder(133840, 'dodo', 50, date(1201, 1, 1), 'justin'),
                         productOrderBuilder(130090, '', None, date(1201, 1, 1), ''),
                         productOrderBuilder(203432, 'bonjour', 2000, date(1201, 1, 1), 'jf'),
                         productOrderBuilder(133045, 'allo', 100, date(1201, 1, 1), 'jb')]

    def testOrderWODateLoading(self):
        '''
        Order must be able to load its ProductOrders from an excel file without
        the date in it, get its length and pop left its whole ProductOrder list.
        '''
        order = Order()
        order.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile1.xls'), False)
        result = []
        for i in range(len(order)):
            result.append(order.popLeft())
        i = i
        self.assertListEqual(result, self.ATTENDED_RESULTS1, 'Order failed to its ProductOrder list from an excel file, get its length and popLeft its whole ProductOrder list')
        
    def testOrderWDateLoading(self):
        '''
        Order must be able to load its ProductOrders from an excel file wit
        the date in it, get its length and pop right its whole ProductOrder list.
        '''
        order = Order()
        order.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile2.xls'), True)
        result = []
        for i in range(len(self.order)):
            result.append(self.order.popRight())
        i = i
        self.assertListEqual(result, self.ATTENDED_RESULTS2, 'Order failed to its ProductOrder list from an excel file, get its length and popRight its whole ProductOrder list')
        
class filterOderTest(unittest.TestCase):
    ATTENDED_RESULTS = [productOrderBuilder(203432, 'bonjour', 2000, date.today(), 'jf admin'),
                        productOrderBuilder(130090, 'prout', 200, date.today(), 'jb'),
                        productOrderBuilder(133840, 'dod', 50, date.today(), 'justin')]
    
    def testFilterOrder(self):
        '''
        Order must be able to filter and remove the bad ProductOrder and those
        already ordered.
        The filters are:
            - imcomplete or incoherent ProductOrder.
            - Already ordered in the last 20 days ProductOrder, except if employee is the admin.
        '''
        order1 = Order()
        order2 = Order()
        order1.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile3.xls'), False)
        order2.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile4.xls'), True)
        order1.filter(order2)
        result = []
        for i in range(len(order1)):
            result.append(order1.popLeft())
        i = i
        self.assertListEqual(result, self.ATTENDED_RESULTS, 'Order failed to filter and remove the bad and already ordered ProductOrder.')
        
class clearAndSaveTest (unittest.TestCase):
    ATTENDED_RESULTS = []
    
    def setup(self):
        '''
        Setup the test case by loading the contant of the files for restoration
        at teardown.
        '''
        self.__originalFile1 = Order()
        self.__originalFile2 = Order()
        self.__originalFile1.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTest5.xls'), False)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()