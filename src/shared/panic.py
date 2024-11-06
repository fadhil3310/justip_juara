from datetime import datetime
from inspect import Traceback
import sys
import os
from time import time
from traceback import TracebackException
from types import FrameType, TracebackType

JUSTIP_DATA_PATH =  os.getenv('APPDATA') + '/justip'
LOG_PATH = JUSTIP_DATA_PATH + '/aku_takut.log'

bypass_handling = False
handling_exception_now = False

def except_hook(exctype, value, traceback: TracebackType):
    if exctype != KeyboardInterrupt and bypass_handling == False and handling_exception_now == False:
        panic(value, traceback.tb_frame)
    else:
        sys.__excepthook__(exctype, value, traceback)
        
def write_log(e, tb_frame: FrameType):
    if os.path.exists(JUSTIP_DATA_PATH) == False:
        os.mkdir(JUSTIP_DATA_PATH)

    f = open(LOG_PATH, "a")
    f.write(str(datetime.now()) + ": " + str(e) + " " + str(tb_frame) + "\n")
    f.close()

def panic(e, tb_frame: FrameType):
    handling_exception_now = True
    print("Detail error:", e, tb_frame)
    write_log(e, tb_frame)
    print("Error telah ditulis ke log")
    print("Menutup aplikasi..")
    exit()
