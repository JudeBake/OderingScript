'''
Created on 2014-01-14

@author: julienbacon
'''

from datetime import date
import os

class Log:
    '''
    Log is a list of messages about what happens during the OrderingScript
    process.
    
    It provides the following interfaces:
        - Log a message in the list.
        - Save its message list in a text file.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__msgList = list()
        
    def logMsg(self, msg):
        '''
        Log new messages.
        '''
        self.__msgList.append(msg)
        
    def getMsgList(self):
        '''
        Get the whole message list.
        '''
        return self.__msgList
        
    def outputLog(self, destinationPath):
        '''
        Output the log messages at the desired location.
        '''
        currentDate = date.today()
        logFile = open(os.path.join(destinationPath, 'Log_' + \
                                    currentDate.strftime('%d-%m-%Y')) +'.txt', 'w+')
        for msg in self.__msgList:
            logFile.write(msg + '\n')
        logFile.flush()
        logFile.close()
        
        