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
    __orderWODate = Order()
    __orderWDate = Order()

    def testOrderWODateLoading(self):
        '''
        Order must be able to load its ProductOrders from an excel file without
        the date in it, get its length and pop left its whole ProductOrder list.
        '''
        self.__orderWODate.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile1.xls'), False)
        result = []
        for i in range(len(self.__orderWODate)):
            result.append(self.__orderWODate.popLeft())
        i = i
        self.assertListEqual(result, self.ATTENDED_RESULTS1, 'Order failed to its ProductOrder list from an excel file, get its length and popLeft its whole ProductOrder list')
        
    def testOrderWDateLoading(self):
        '''
        Order must be able to load its ProductOrders from an excel file wit
        the date in it, get its length and pop right its whole ProductOrder list.
        '''
        self.__orderWDate.loadOrder(os.path.join(TEST_FILE_ROOT, 'OrderTestFile2.xls'), True)
        result = []
        for i in range(len(self.__orderWDate)):
            result.append(self.__orderWDate.popRight())
        i = i
        self.assertListEqual(result, self.ATTENDED_RESULTS2, 'Order failed to its ProductOrder list from an excel file, get its length and popRight its whole ProductOrder list')
        
class filterOderTest(unittest.TestCase):
    ATTENDED_RESULTS = []

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()