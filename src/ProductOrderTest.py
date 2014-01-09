'''
Created on 2014-01-09

@author: julienbacon
'''

from ProductOrder import ProductOrder
import unittest

class ProductNbSetterGetterTest(unittest.TestCase):
    TEST_VALUES = (133439, 132090, 103600)
    __productOrder = ProductOrder()
    
    def testProductNbSetterAndGetter(self):
        '''
        ProductOrder must be able to set and its product number field.
        '''
        for value in self.TEST_VALUES:
            self.__productOrder[ProductOrder.PROD_NB_KEY] = value
            result = self.__productOrder[ProductOrder.PROD_NB_KEY]
            self.assertEqual(result, value, 'ProductOrder failed to set and get its product number field.')
            
class DescripttionSetterGetterTest(unittest.TestCase):
    TEST_VALUE = ('aaaaa', 'adbawubfa;jfb', ';ajbfoeubfaj')
    __productOrder = ProductOrder()
    
    def testDescriptionSetterAndGetter(self):
        '''
        ProductOrder must be able to set and get its product description field.
        '''
        for value in self.TEST_VALUE:
            self.__productOrder[ProductOrder.DESC_KEY] = value
            result = self.__productOrder[ProductOrder.DESC_KEY]
            self.assertEqual(result, value, 'ProduvtOrder failed to set and get its product description field.')
            
class QtyToOrderSetterGetterTest(unittest.TestCase):
    TEST_VALUE = (1, 1000, 695, 18265)
    __productOrder = ProductOrder()
    
    def testQtyToOrderSetterAndGetter(self):
        '''
        ProductOrder must be able to set and get its quanty to order field.
        '''
        for value in self.TEST_VALUE:
            self.__productOrder[ProductOrder.QTY_TO_ORDER_KEY] = value
            result = self.__productOrder[ProductOrder.QTY_TO_ORDER_KEY]
            self.assertEqual(result, value, 'ProductOrder failed to set and get its quantity to order field.')
            
class DateSetterGetterTest(unittest.TestCase):
    TEST_VALUE = (('01/01/01', '01/01/01'), ('31/12/2014', '31/12/14'),
                  ('15/06/10', '15/06/10'), ('27/07/3333', '27/07/33'))
    __productOrder= ProductOrder()
    
    def testDateSetterAndGetter(self):
        '''
        ProductOrder must be able to set and get its date field.
            - input string format: dd/mm/yy or dd/mm/yyyy.
            - output string format: dd/mm/yy
        '''
        for value, attendedResult in self.TEST_VALUE:
            self.__productOrder[ProductOrder.DATE_KEY] = value
            result = self.__productOrder[ProductOrder.DATE_KEY]
            self.assertEqual(result, attendedResult, 'ProductOrder failed to set and get its date field.')
            
class CmpProductOrderTest(unittest.TestCase):
    TEST_VALUE = ((133439, 133439, True), (132090, 103600, False))
    __productOrder1 = ProductOrder()
    __productOrder2 = ProductOrder()
    
    def testCmpProductOrder(self):
        '''
        ProductOrder must be able to figure if it orders the same product than
        an other ProductOrder.
        '''
        for value1, value2, attendedResult in self.TEST_VALUE:
            self.__productOrder1[ProductOrder.PROD_NB_KEY] = value1
            self.__productOrder2[ProductOrder.PROD_NB_KEY] = value2
            result = self.__productOrder1 == self.__productOrder2
            self.assertEqual(result, attendedResult, 'ProductOrder failed to figure if it orders the same product than an other ProductOrder')
            
class ProductOrderStrGetterTest(unittest.TestCase):
    TEST_VALUE = ((133658, 'abcd', 100, '13/10/37', ';133658;abcd;100;13/10/37'),
                  (103800, 'gdtkcvyl', 753, '01/05/14', ';103800;gdtkcvyl;753;01/05/14'))
    __productOrder = ProductOrder()
    
    def testProductOrderStrGetter(self):
        '''
        ProductOrder must be able to get a string representaion of its data
        in the format ;productNb;description;qtyToOrder;date.
        '''
        for pNb, desc, qty, orderDate, attendedResult in self.TEST_VALUE:
            self.__productOrder[ProductOrder.PROD_NB_KEY] = pNb
            self.__productOrder[ProductOrder.DESC_KEY] = desc
            self.__productOrder[ProductOrder.QTY_TO_ORDER_KEY] = qty
            self.__productOrder[ProductOrder.DATE_KEY] = orderDate
            result = self.__productOrder.getProductOrderStr()
            self.assertEqual(result, attendedResult, 'ProductOrder failed to get a string representaion of its data in the format productNb;description;qtyToOrder;date')
            
class DeltaProductOrderTest(unittest.TestCase):
    TEST_VALUE = (('01/01/01', '01/01/01', 0), ('01/07/14', '31/07/14', -30),
                  ('27/11/37', '03/12/37', -6), ('15/12/2999', '10/01/3000', -26),
                  ('20/02/12', '06/03/12', -15), ('15/12/14', '10/12/14', 5))
    __productOrder1 = ProductOrder()
    __productOrder2 = ProductOrder()
    
    def testDeltaProductOrder(self):
        '''
        ProductOrder must be able to calculate the number of days between itself
        and an other ProductOrder.
        '''
        for value1, value2, attendedResult in self.TEST_VALUE:
            self.__productOrder1[ProductOrder.DATE_KEY] = value1
            self.__productOrder2[ProductOrder.DATE_KEY] = value2
            result = self.__productOrder1.deltaProductOrder(self.__productOrder2)
            self.assertEqual(result, attendedResult, 'ProductOrder failed to calculate the number of days between itself and an other ProductOrder.')
        
if __name__ == "__main__":
    unittest.main()
        