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

    def __init__(self, to, cc):
        '''
        Constructor
        '''
        self.__to = to
        self.__cc = cc
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
        bodyStr = '<HTML><BODY>'
        for line in self.__body:
            bodyStr = '<BR>'.join((bodyStr, line))
        bodyStr = bodyStr + '</BODY></HTML>'
        cmd = 'thunderbird -compose to=\"%s\",cc=\"%s\"subject=\"A COMMANDER\",format=\"1\",body=\"%s\"' % (self.__to, self.__cc, bodyStr)
        os.system(cmd)
