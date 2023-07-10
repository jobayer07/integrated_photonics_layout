import sys
sys.path.append(r'C:\Users\mh220218\Documents\My Assignments\Design Work\00Resources\aimphotonics_nazca')
sys.path.append(r'C:\Users\mh220218\Documents\My Assignments\Design Work\00Resources\aimphotonics_nazca\internal')

import nazca as nd
import AIMPhotonics as AIM
from AIMPhotonics import *
#from generator import * #macroBuilder

from generator.cell import *

#SEAM Waveguide

ps1 = mmi2x2(length=15, width=4, taper_length=5, taper_width=1, taper_separation=1.3, xs='SEAM Waveguide', waveguide_width=0.31, label='').put()


nd.export_gds(filename='Smmi_15Length_4Width_1TaperWidth_1.3TaperSep_5TaperLength.gds')

print('Done')


#Delay
import time
time.sleep(3) # Sleep for 3 seconds

#Restart Kernel
import os
os._exit(00)