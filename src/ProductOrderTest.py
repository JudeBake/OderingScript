'''
Created on 2014-01-09

@author: julienbacon
'''

from datetime import date
from ProductOrder import ProductOrder
import unittest

class ProductNbSetterGetterTest(unittest.TestCase):
    TEST_VALUES = (133439, 132090, 103600)
    
    def testProductNbSetterAndGetter(self):
        '''
        ProductOrder must be able to set and its product number field.
        '''
        prodOrder = ProductOrder()
        for value in self.TEST_VALUES:
            prodOrder[ProductOrder.PROD_NB_KEY] = value
            result = prodOrder[ProductOrder.PROD_NB_KEY]
            self.assertEqual(result, value, 'ProductOrder failed to set and get its product number field.')
            
class DescripttionSetterGetterTest(unittest.TestCase):
    TEST_VALUE = ('aaaaa', 'adbawubfa;jfb', ';ajbfoeubfaj')
    
    def testDescriptionSetterAndGetter(self):
        '''
        ProductOrder must be able to set and get its product description field.
        '''
        prodOrder = ProductOrder()
        for value in self.TEST_VALUE:
            prodOrder[ProductOrder.DESC_KEY] = value
            result = prodOrder[ProductOrder.DESC_KEY]
            self.assertEqual(result, value, 'ProduvtOrder failed to set and get its product description field.')
            
class QtyToOrderSetterGetterTest(unittest.TestCase):
    TEST_VALUE = (1, 1000, 695, 18265)
    prodOrder = ProductOrder()
    
    def testQtyToOrderSetterAndGetter(self):
        '''
        ProductOrder must be able to set and get its quanty to order field.
        '''
        prodOrder = ProductOrder()
        for value in self.TEST_VALUE:
            prodOrder[ProductOrder.QTY_TO_ORDER_KEY] = value
            result = prodOrder[ProductOrder.QTY_TO_ORDER_KEY]
            self.assertEqual(result, value, 'ProductOrder failed to set and get its quantity to order field.')
            
class DateSetterGetterTest(unittest.TestCase):
    TEST_VALUE = (('01/01/01', '01/01/2001'), ('31/12/2014', '31/12/2014'),
                  ('15/06/10', '15/06/2010'), ('27/07/3333', '27/07/3333'),
                  (date(1900, 2, 3), '03/02/1900'))
    
    def testDateSetterAndGetter(self):
        '''
        ProductOrder must be able to set and get its date field.
            - input string format: dd/mm/yy or dd/mm/yyyy or date object.
            - output string format: dd/mm/yyyy
        '''
        prodOrder = ProductOrder()
        for value, attendedResult in self.TEST_VALUE:
            prodOrder[ProductOrder.DATE_KEY] = value
            result = prodOrder[ProductOrder.DATE_KEY]
            self.assertEqual(result, attendedResult, 'ProductOrder failed to set and get its date field.')
            
class EmpoyeeSetterGetterTest(unittest.TestCase):
    TEST_VALUE = ('jb', 'jf', 'justin')
    
    def testEmpoyeeSetterAndGetterTest(self):
        '''
        ProductOrder must be able to set and get its employee field.
        '''
        prodOrder = ProductOrder()
        for value in self.TEST_VALUE:
            prodOrder[ProductOrder.EMPLOYEE_KEY] = value;
            result = prodOrder[ProductOrder.EMPLOYEE_KEY]
            self.assertEqual(result, value, 'ProductOrder failed to set and get its employee field.')
            
class CmpProductOrderTest(unittest.TestCase):
    TEST_VALUE = ((133439, 133439, True), (132090, 103600, False))
    
    def testCmpProductOrder(self):
        '''
        ProductOrder must be able to figure if it orders the same product than
        an other ProductOrder.
        '''
        prodOrder1 = ProductOrder()
        prodOrder2 = ProductOrder()
        for value1, value2, attendedResult in self.TEST_VALUE:
            prodOrder1[ProductOrder.PROD_NB_KEY] = value1
            prodOrder2[ProductOrder.PROD_NB_KEY] = value2
            result = prodOrder1 == prodOrder2
            self.assertEqual(result, attendedResult, 'ProductOrder failed to figure if it orders the same product than an other ProductOrder')
            
class ProductOrderStrGetterTest(unittest.TestCase):
    TEST_VALUE = ((133658, 'abcd', 100, '13/10/37', 'jb', '100 X 133658 abcd'),
                  (103800, 'gdtkcvyl', 753, '01/05/14', None, '753 X 103800 gdtkcvyl'))
    prodOrder = ProductOrder()
    
    def testProductOrderStrGetter(self):
        '''
        ProductOrder must be able to get a string representaion of its data
        in the format ;productNb;description;qtyToOrder;date.
        '''
        for pNb, desc, qty, orderDate, empl, attendedResult in self.TEST_VALUE:
            self.prodOrder[ProductOrder.PROD_NB_KEY] = pNb
            self.prodOrder[ProductOrder.DESC_KEY] = desc
            self.prodOrder[ProductOrder.QTY_TO_ORDER_KEY] = qty
            self.prodOrder[ProductOrder.DATE_KEY] = orderDate
            self.prodOrder[ProductOrder.EMPLOYEE_KEY] = empl
            result = self.prodOrder.getProductOrderStr()
            self.assertEqual(result, attendedResult, 'ProductOrder failed to get a string representaion of its data in the format productNb;description;qtyToOrder;date')
            
class DeltaProductOrderTest(unittest.TestCase):
    TEST_VALUE = (('01/01/01', '01/01/01', 0), ('01/07/14', '31/07/14', -30),
                  ('27/11/37', '03/12/37', -6), ('15/12/2999', '10/01/3000', -26),
                  ('20/02/12', '06/03/12', -15), ('15/12/14', '10/12/14', 5))
    prodOrder1 = ProductOrder()
    prodOrder2 = ProductOrder()
    
    def testDeltaProductOrder(self):
        '''
        ProductOrder must be able to calculate the number of days between itself
        and an other ProductOrder.
        '''
        for value1, value2, attendedResult in self.TEST_VALUE:
            self.prodOrder1[ProductOrder.DATE_KEY] = value1
            self.prodOrder2[ProductOrder.DATE_KEY] = value2
            result = self.prodOrder1.deltaProductOrder(self.prodOrder2)
            self.assertEqual(result, attendedResult, 'ProductOrder failed to calculate the number of days between itself and an other ProductOrder.')
            
class ValifityGetterTest(unittest.TestCase):
    TEST_VALUE = ((None, 'asfefg', 100, '01/01/01', 'jb', False),
                      (103030, None, 200, '01/01/01', 'jf', False),
                      (103486, 'afeohg', None, '01/01/01','justin', False),
                      (133036, 'kajsbeo', 1000, '01/0101', 'guy', False),
                      (133025, 'afeoboi', 25, '01/01/01', None, False),
                      (None, 'aibef', 25, '01/01/01/01', 'Daniel', False),
                      (123945, 'eouty', 0, '10/10/10', 'jb', False),
                      (124666, 'jafoe;', 100, None, 'jb', False),
                      (133045, 'aiefo', 3, '01/01/01', 'Daniel', True))
    prodOrder = ProductOrder()
    
    def testValidityGetter(self):
        '''
        ProductOrder must be able to figure if it's valid or not.
        '''
        for pNb, desc, qty, date, empl, attendedResult in self.TEST_VALUE:
            self.prodOrder[ProductOrder.PROD_NB_KEY] = pNb
            self.prodOrder[ProductOrder.DESC_KEY] = desc
            self.prodOrder[ProductOrder.QTY_TO_ORDER_KEY] = qty
            self.prodOrder[ProductOrder.DATE_KEY] = date
            self.prodOrder[ProductOrder.EMPLOYEE_KEY] = empl
            result = self.prodOrder.isValid()
            self.assertEqual(result, attendedResult, 'ProductOrder failed to figure if it\'s valid or not.')
        
if __name__ == "__main__":
    unittest.main()
        