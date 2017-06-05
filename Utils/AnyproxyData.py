# -*- coding:utf-8 -*-
import os
from time import sleep

from Utils.TimeUtil import timestamp


def run_Anyproxy(command):
    try:
        a=os.system(command)
        b=os.popen(command)
        sleep(3)
    except IOError as err:
        print(err)
    return b

if __name__ == '__main__':

    # run_Anyproxy('appium')

    print()

    aa = 'anyproxy '+'--file ' + os.path.abspath('../Resources/') + '\%s' % timestamp('%Y-%m-%d')+'.json'
    print(aa)
    run_Anyproxy(aa)
    bb='exit()'
    sleep(3)
    run_Anyproxy(bb)