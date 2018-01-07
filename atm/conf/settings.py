##configration settings
import os,sys
import logging

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
##print(BASE_DIR)
DATABASE={
    'engineer':'file',
    'name':'account',
    'path':os.path.join(BASE_DIR,'data')}
##print(DATABASE)

LOG_LEVEL=logging.INFO

LOG_TYPE={
    'transaction':r'transaction.log',
    'access':r'access.log'}

LOG_PATH=os.path.join(BASE_DIR,'log')
##print(LOG_PATH)

TRANSACTION_TYPE = {
    'repay':{'action':'plus','interest':0},
    'withdraw':{'action':'minus','interest':0},
    'transfer':{'action':'minus','interest':0}
    }
