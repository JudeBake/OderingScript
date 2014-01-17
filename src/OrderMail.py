'''
Created on 2014-01-16

@author: julienbacon
'''

import os

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
        bodyStr = '%2c'
        for line in self.__body:
            bodyStr = '%0d0a'.join((bodyStr, line))
		l = bodyStr.split(' ')
		bodyStr = '%20'.join(l)
        cmd = 'thunderbird -compose to=\'%s\',subject=\'commande\',body=\'%s)\'' % (self.__to, bodyStr)
        print(cmd)
        os.system(cmd)
