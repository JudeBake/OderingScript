'''
Created on 2014-01-16

@author: julienbacon
'''

class OrderMail:
    '''
    OrderMail is the wrapper of the thunderbird command line interface.
    
    It provides the following interfaces:
        - Set the To field of the mail.
        - Add lines to the body of the mail.
        - Generate the mail.
    '''

    def __init__(self, to):
        '''
        Constructor
        '''
        self.__to = to
        self.__body = []
        
    def addLineToBody(self, line):
        '''
        Add a line to the body of the OrderMail.
        '''
        self.__body.append(line)
        
    def generate(self):
        '''
        Generate the mail.
        '''
