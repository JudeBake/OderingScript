'''
Created on 2014-01-08

@author: julienbacon
'''

from datetime import date
import re
import unicodedata

class ProductOrderError(Exception):
    '''
    Base exception for product error
    '''
    pass

class ProductOrder:
    '''
    ProductOrder is a wrapper of dict that is the rep of a product order.
    It contains the following info:
        - The product number: "productNb" (as integer).
        - The description: "description" (as string).
        - The quantity to order: "qtyToOrder" (as integer)
        - The date the order is (has been) made: "date" (as date)
        
    It give the following interfaces:
        - Set product number as Dictionnary behavior
        - Get product Number as Dictionnary behavior
        - Set product description as Dictionnary behavior
        - Get product desciption as Dictionnary behavior
        - Set quantity to order as Dictionnary behavior
        - Get quantity to order as Dictionnary behavior
        - Convert ProductOrder to String
        - Compare ProductOrder by returning the number of days between orders
    '''
    PROD_NB_KEY = "productNb"
    DESC_KEY = "description"
    QTY_TO_ORDER_KEY = "qtyToOrder"
    DATE_KEY = "date"
    EMPLOYEE_KEY = "employee"
    KEYS = (PROD_NB_KEY, DESC_KEY, QTY_TO_ORDER_KEY, DATE_KEY, EMPLOYEE_KEY)
    ROWS = (0, 1, 2, 3)

    def __computeDateString(self, string):
        '''
        Compute the date inputed date string into a date.
        '''
        YEAR_IDX = 2
        MONTH_IDX = 1
        DAY_IDX = 0
        #paturn defining the date string format (dd/mm/yy or dd/mm/yyyy)
        datePaturn = re.compile(r'''
                            ^                #beginning of the string
                            (\d{2})          #day
                            \D               #separator
                            (\d{2})          #month
                            \D               #separator
                            (\d{2}|\d{4})    #year
                            $                #end of string
                            ''', re.VERBOSE)
        #test the inputed date string and get its values if valid
        try:
            dateValues = list(datePaturn.search(string).groups())
        except:
            dateValues = list()
        #convert the string list into an integer list
        dateValues = [int(element) for element in dateValues]
        #if the input string has 2 digit for the year, add to it the thousands
        #and undreds
        if dateValues and dateValues[YEAR_IDX] < 100:
            currentYearThousands = int(date.today().year / 1000) * 1000
            dateValues[YEAR_IDX] += currentYearThousands
        try:
            orderDate = date(dateValues[YEAR_IDX], dateValues[MONTH_IDX],
                             dateValues[DAY_IDX])
        except:
            orderDate = None
        return orderDate
        
    def __init__(self):
        '''
        Constructor
        '''
        self.__orderData = {}
        #set all fields to None
        for key in self.KEYS:
            self.__orderData[key] = None
            
    def __getitem__(self, key):
        '''
        Wrapper of dict["key"]
        For the date field the return is a string in the format dd/mm/yyyy.
        '''
        #if date field is asked, return it in string of the format dd/mm/yy
        if key == self.DATE_KEY and self.__orderData[key]:
            return unicode(self.__orderData[key].strftime("%d/%m/%Y"))
        #if other field, simply return it as is
        else:
            return self.__orderData[key]
    
    def __setitem__(self, key, value):
        '''
        Wrapper of dict["key"] = value
        For the date field the value must be a string in the format dd/mm/yy. 
        '''
        #if setting date field, process it into a date object before assignation
        if key == self.DATE_KEY:
            if type(value).__name__ == 'unicode':
                self.__orderData[key] = \
                    self.__computeDateString(unicodedata.normalize('NFKD', value)\
                                             .encode('ascii', 'ignore'))
            else:
                self.__orderData[key] = None
        #if setting quantity to order, set as number, as u'x' or as None
        elif key == self.QTY_TO_ORDER_KEY:
            if value and value.isdigit():
                self.__orderData[key] = value
            elif value == u'X' or value == u'x':
                self.__orderData[key] = value.lower()
            else:
                self.__orderData[key] = None
        #if setting product number, set as 6 digit first, as u'x' or as None
        elif key == self.PROD_NB_KEY:
            if value and value[:6].isdigit():
                self.__orderData[key] = value;
            elif value == u'X' or value == u'x':
                self.__orderData[key] = value.lower()
            else:
                self.__orderData[key] = None
        #if other field, simply assign it
        else:
            self.__orderData[key] = value
            
    def prodNbCmp(self, productOrder):
        '''
        Compare the product number field of two product orders.
        '''
        return self.__orderData[self.PROD_NB_KEY][:6] == productOrder[self.PROD_NB_KEY][:6]
        
    def getProductOrderStr(self):
        '''
        Construct and return a string from the data of the product order.
        Return an empty string if no data or incomplete data.
        The string returned doesn't contain the date nor the employee.
        '''
        string = u''
        if self.__orderData[self.QTY_TO_ORDER_KEY]:
            string = u' '.join((string, self.__orderData[self.QTY_TO_ORDER_KEY] + ' X'))
        else:
            string = u' '.join((string, u'N/A X'))
        if self.__orderData[self.PROD_NB_KEY]:
            string = u' '.join((string, self.__orderData[self.PROD_NB_KEY]))
        else:
            string = u' '.join((string, u'N/A'))
        if self.__orderData[self.DESC_KEY]:
            string = u' '.join((string, self.__orderData[self.DESC_KEY]))
        else:
            string = u' '.join((string, u'N/A'))
        string = string.lstrip()
        return string
    
    def deltaProductOrder(self, productOrder):
        '''
        Calculate the number of days between two ProductOrders.
        '''
        return (self.__orderData[ProductOrder.DATE_KEY] - 
                productOrder.__orderData[ProductOrder.DATE_KEY]).days
                
    def getProductOrderAge(self):
        currentDate = date.today()
        return abs((self.__orderData[self.DATE_KEY] - currentDate).days)
                
    def isValid(self):
        '''
        Check the validity of a product order.
        '''
        validity = True
        #look for None data, and 0 quantity
        for key in self.KEYS:
            if not self.__orderData[key]:
                validity = False
        if self.__orderData[self.QTY_TO_ORDER_KEY] == u'0':
            validity = False
        return validity
            