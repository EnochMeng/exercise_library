##launch program

import os,sys

dir_atm=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,dir_atm)
##add atm directories to system environment path for the operation below

from core import main

if __name__=='__main__':
    main.run()
    
