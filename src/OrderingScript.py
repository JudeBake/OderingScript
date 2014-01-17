'''
OrderingScript -- Ordering Script to order by sending email to Sebastien

OrderingScript is a Ordering Script to order by sending email to Sebastien

@author:     JudeBake

@copyright:  2014 JudeBake. All rights reserved.

@license:    GNU

@contact:    julien.bacon.1@gmail.com
@deffield    updated: Updated
'''

import ctypes
import sys
import os
import winsound

#add the project path to sys.path
sys.path.append(os.path.join(os.getcwd()))

from Log import Log
from Order import Order
from OrderMail import OrderMail

#get the files path
dailyOrderFile = sys.argv[1]
previousOrderFile = sys.argv[2]
outputPath = '..\\..\\'
audioPath = '..\\'

#notify the closing of libreOffice and kill it
a = ctypes.windll.user32.MessageBoxA(0, 'LibreOffice fermera dans 60 seconde.',
                                     '!!!Killing Notification!!!', 0)

#kill LibreOffice !!!!!!!!!!!NEED TO BE MODIFIED!!!!!!!!!!!!
os.system('taskkill /f /im soffice.bin')

#instanciate the log file
log = Log()

#load the data from the input files
dailyOrder = Order(log)
previousOrder = Order(log)
try:
    dailyOrder.loadOrder(dailyOrderFile)
except:
    #if nothing to order, simply log it and exit
    log.logMsg('Rien a commander.')
    log.outputLog(outputPath)
    sys.exit(0)
try:
    previousOrder.loadOrder(previousOrderFile)
except:
    pass

#filter the daily order data
dailyOrder.filter(previousOrder)

#generate the mail
orderMail = OrderMail('sebastien.levesque@addison-electronique.com')
for order in dailyOrder.getOrderList():
    orderMail.addLineToBody(order.getProductOrderStr())
#orderMail.generate()

#transfert data to previousOrder and clean up dailyOrder
#for i in range(len(dailyOrder)):
#    previousOrder.append(dailyOrder.popLeft())
#dailyOrder.save(dailyOrderFile)
#previousOrder.save(previousOrderFile)

#save the log
#log.outputLog(outputPath)

#notify that the mail is ready to send
winsound.PlaySound(os.path.join(audioPath, 'orderingscript.wav'), winsound.SND_FILENAME)
