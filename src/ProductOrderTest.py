'''
Created on 2014-01-09

@author: julienbacon
'''

from datetime import date
from ProductOrder import ProductOrder
import unittest

class ProductNbSetterGetterTest(unittest.TestCase):
    TEST_VALUES = (u'133439', u'132090', u'103600')
    
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
    TEST_VALUE = (u'aaaaa', u'adbawubfa;jfb', u';ajbfoeubfaj')
    
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
    TEST_VALUE = ((u'1', u'1'), (u'1000', u'1000'), (u'695', u'695'),
                  (u'18265', u'18265'), (u'X', u'x'), (u'a', None), (u'x', u'x'))
    prodOrder = ProductOrder()
    
    def testQtyToOrderSetterAndGetter(self):
        '''
        ProductOrder must be able to set and get its quanty to order field.
        '''
        prodOrder = ProductOrder()
        for value, attendedResult in self.TEST_VALUE:
            prodOrder[ProductOrder.QTY_TO_ORDER_KEY] = value
            result = prodOrder[ProductOrder.QTY_TO_ORDER_KEY]
            self.assertEqual(result, attendedResult, 'ProductOrder failed to set and get its quantity to order field.')
            
class DateSetterGetterTest(unittest.TestCase):
    TEST_VALUE = ((u'01/01/01', u'01/01/2001'), (u'31/12/2014', u'31/12/2014'),
                  (u'15/06/10', u'15/06/2010'), (u'27/07/3333', u'27/07/3333'))
    
    def testDateSetterAndGetter(self):
        '''
        ProductOrder must be able to set and get its date field.
            - input string format: dd/mm/yy or dd/mm/yyyy.
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
    TEST_VALUE = ((u'133439', u'133439**', True), (u'132090', u'103600', False))
    
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
    TEST_VALUE = ((u'133658', u'abcd', u'100', u'13/10/37', u'jb', u'100 X 133658 abcd'),
                  (u'103800', u'gdtkcvyl', u'753', u'01/05/14', None, u'753 X 103800 gdtkcvyl'),
                  (None, u'utfiyt', None, None, None, u'N/A X N/A utfiyt'),
                  (u'134654**', u'itfkgc', u'X', u'13/07/45', u'jf', u'x X 134654** itfkgc'))
    prodOrder = ProductOrder()
    
    def testProductOrderStrGetter(self):
        '''
        ProductOrder must be able to get a string representaion of its data
        in the format qty X productNb description.
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
    TEST_VALUE = ((u'01/01/01', u'01/01/01', 0), (u'01/07/14', u'31/07/14', -30),
                  (u'27/11/37', u'03/12/37', -6), (u'15/12/2999', u'10/01/3000', -26),
                  (u'20/02/12', u'06/03/12', -15), (u'15/12/14', u'10/12/14', 5))
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
            
class ProductOrderAgeGetterTest(unittest.TestCase):
    TEST_VALUE = ((u'01/01/14', abs((date(2014, 1, 1) - date.today()).days)),
                  (u'01/01/13', abs((date(2013, 1, 1) - date.today()).days)),
                  (u'14/01/14', abs((date(2014, 1, 14) - date.today()).days)))
    
    def testProductOrderAgeGetter(self):
        '''
        ProductOrder must be able to get its age from current date.
        '''
        prodOrder = ProductOrder()
        for value, attendedResult in self.TEST_VALUE:
            prodOrder[ProductOrder.DATE_KEY] = value
            result = prodOrder.getProductOrderAge()
            self.assertEqual(result, attendedResult, 'ProductOrder fails to get its age.')
            
class ValifityGetterTest(unittest.TestCase):
    TEST_VALUE = ((None, u'asfefg', u'100', u'01/01/01', u'jb', False),
                      (u'103030', None, u'200', u'01/01/01', u'jf', False),
                      (u'103486', u'afeohg', None, u'01/01/01', u'justin', False),
                      (u'133036', u'kajsbeo', u'1000', u'01/0101', u'guy', False),
                      (u'133025', u'afeoboi', u'25', u'01/01/01', None, False),
                      (None, u'aibef', u'25', u'01/01/01/01', u'Daniel', False),
                      (u'123945', u'eouty', u'0', u'10/10/10', u'jb', False),
                      (u'124666', u'jafoe;', u'100', None, u'jb', False),
                      (u'133045', u'aiefo', u'3', u'01/01/01', u'Daniel', True))
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
        