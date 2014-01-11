'''
Created on 2014-01-09

@author: julienbacon
'''

from datetime import date
from ProductOrder import ProductOrder
from Order import Order
import os
import unittest

TEST_FILE_ROOT = '..\test_files'

def productOrderBuilder(prodNb, desc, qty, date):
    prodOrder = ProductOrder()
    prodOrder[ProductOrder.PROD_NB_KEY] = prodNb
    prodOrder[ProductOrder.DESC_KEY] = desc
    prodOrder[ProductOrder.QTY_TO_ORDER_KEY] = qty
    prodOrder[ProductOrder.DATE_KEY] = date
    return prodOrder
    
class OrderLoadingTest(unittest.TestCase):
    ATTENDED_RESULTS = [productOrderBuilder(133045, 'allo', 100, date.today().strftime("%d/%m/%y")),
                        productOrderBuilder(20432, 'bonjour', 2000, date.today().strftime("%d/%m/%y"))]
    
    __order = Order()

    def testOrderLoading(self):
        '''
        Order must be able to load its ProductOrders from an excel file in read
        only mode and get its whole ProductOrder list.
        '''
        self.__order.loadOrder(os.path.join((TEST_FILE_ROOT, self.__name__)))
        result = self.__order.getOrderList()
        self.assertListEqual(result, self.ATTENDED_RESULTS, 'Order failed to its ProductOrder list from an excel file and get its entire ProductOrder list')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()