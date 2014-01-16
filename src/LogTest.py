'''
Created on 2014-01-14

@author: julienbacon
'''

from datetime import date
from Log import Log
import os
import unittest

TEST_FILE_ROOT = r'..\test_files'

class logMsgTest(unittest.TestCase):
    TEST_VALUES = ['allo', 'bonjour', 'comment ca va']

    def testLogMsg(self):
        '''
        Log must be able to log new messages.
        '''
        log = Log()
        for msg in self.TEST_VALUES:
            log.logMsg(msg)
        self.assertListEqual(log.getMsgList(), self.TEST_VALUES, 'Log isn\'t able to log new messages')
        
class outputLogTest(unittest.TestCase):
    TEST_VALUES = ['eugab', ';equbfa', 'uiqefajbaiu', 'abufuif;avn ']
    
    def tearDown(self):
        currentDate = date.today()
        os.remove(os.path.join(TEST_FILE_ROOT, 'Log_' + currentDate.strftime('%d-%m-%Y') + '.txt'))
        
    def testOutputLog(self):
        '''
        Log must be able to output its message list.
        '''
        currentDate = date.today()
        log = Log()
        for msg in self.TEST_VALUES:
            log.logMsg(msg)
        log.outputLog(TEST_FILE_ROOT)
        f = open(os.path.join(TEST_FILE_ROOT, 'Log_' + currentDate.strftime('%d-%m-%Y') + '.txt'), 'r')
        result = f.readlines()
        f.close()
        attendedResult = [msg + '\n' for msg in self.TEST_VALUES]
        self.assertListEqual(result, attendedResult, 'log isn\'t able to output its message list.')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()