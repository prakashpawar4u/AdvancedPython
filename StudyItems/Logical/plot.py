import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rsrp=  [-60, -70, -80, -87, -90, -91, -95, -99, -105, -110, -120]
ul_throughtput= [105, 95, 85, 75, 65 , 55, 45, 35, 25, 15, 0]

plt.plot(rsrp, ul_throughtput, "b")
plt.title('DL Throughput plot')
plt.ylabel('Throughput in Mbps')
plt.xlabel('RSRP on X axis')
plt.savefig('rsrp_tp.pdf')
#plt.show()

