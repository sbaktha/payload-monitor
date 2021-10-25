from matplotlib.pyplot import subplot2grid
import numpy
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.animation as animation
import pandas as pd
import time
import streamlit as st

# Create placeholder canvas and some buttons
placeholder = st.empty()
start_button = st.empty()


# Sent for figure
font = {'size'   : 8}
matplotlib.rc('font', **font)

# Setup figure and subplots
f0 = figure(num = 0, figsize = (12, 8))#, dpi = 100)
f0.suptitle("Payload Sensor", fontsize=12)
ax01 = subplot2grid((3, 2), (0, 0))
ax02 = subplot2grid((3, 2), (0, 1))
ax03 = subplot2grid((3, 2), (1, 0))
ax04 = subplot2grid((3, 2), (1, 1))
ax05 = subplot2grid((3, 2), (2, 0))
# ax03 = subplot2grid((3, 2), (1, 0), colspan=2, rowspan=1)
# ax04 = ax03.twinx()

#tight_layout()

# Set titles of subplots
ax01.set_title('Accelerometer')
ax02.set_title('Magnetometer')
ax03.set_title('Altitude')
ax04.set_title('Temperature')
ax05.set_title('Gyro')

# # set y-limits
# ax01.set_ylim(amin(AccX)-5,amax(AccX)+5)
# ax02.set_ylim(min(MagX)-5,max(MagX)+5)
# ax03.set_ylim(min(Alt)-5,max(Alt)+5)
# ax04.set_ylim(min(Temp)-5,max(Temp)+5)

# set y-limits
ax01.set_ylim(-3,3)
ax02.set_ylim(-50,50)
ax03.set_ylim(50,100)
ax04.set_ylim(20,50)
ax05.set_ylim(20,50)

# set x-limits
ax01.set_xlim(0,50)
ax02.set_xlim(0,50)
ax03.set_xlim(0,50)
ax04.set_xlim(0,50)
ax05.set_xlim(0,50)

# Turn on grids
ax01.grid(True)
ax02.grid(True)
ax03.grid(True)
ax04.grid(True)
ax05.grid(True)

# set label names
# ax01.set_xlabel("x")
# ax01.set_ylabel("py")
# ax02.set_xlabel("t")
# ax02.set_ylabel("vy")
# ax03.set_xlabel("t")
# ax03.set_ylabel("py")
# ax04.set_ylabel("vy")

# Data Placeholders
index = zeros(0)
AccX = zeros(0)
AccY = zeros(0)
AccZ = zeros(0)
MagX = zeros(0)
MagY = zeros(0)
MagZ = zeros(0)
GyrX = zeros(0)
GyrY = zeros(0)
GyrZ = zeros(0)
Alt = zeros(0)
Temp = zeros(0)
# set plots
p011, = ax01.plot(index,AccX,'b-', label="AccX")
p012, = ax01.plot(index,AccY,'g-', label="AccY")
p013, = ax01.plot(index,AccZ,'r-', label="AccZ")

p021, = ax02.plot(index,MagX,'b-', label="MagX")
p022, = ax02.plot(index,MagY,'g-', label="MagY")
p023, = ax02.plot(index,MagZ,'r-', label="MagZ")

p031, = ax03.plot(index,Alt,'b-', label="Altitude")
p041, = ax04.plot(index,Temp,'b-', label="Temperature")

p051, = ax05.plot(index,GyrX,'b-', label="GyrX")
p052, = ax05.plot(index,GyrY,'g-', label="GyrY")
p053, = ax05.plot(index,GyrZ,'r-', label="GyrZ")

# set lagends
ax01.legend([p011,p012,p013], [p011.get_label(),p012.get_label(),p013.get_label()])
ax02.legend([p021,p022,p023], [p021.get_label(),p022.get_label(),p023.get_label()])
ax03.legend([p031], [p031.get_label()])
ax04.legend([p041], [p041.get_label()])
ax05.legend([p051,p052,p053], [p051.get_label(),p052.get_label(),p053.get_label()])


# Data Update
xmin = 0
xmax = 50
x = 0
# file_name = "http://raw.githubusercontent.com/sbaktha/payload-monitor/main/data.csv"
file_name = './testdata2.csv'
def updateData():

    global index
    global AccX
    global AccY
    global AccZ
    global MagX
    global MagY
    global MagZ
    global GyrX
    global GyrY
    global GyrZ
    global Alt
    global Temp

    data = pd.read_csv(file_name)
    index = data['Index']
    ind=data.index.tolist()
    print(ind)
    AccX = data['AccX']
    AccY = data['AccY']
    AccZ = data['AccZ']
    MagX = data['MagX']
    MagY = data['MagY']
    MagZ = data['MagZ']
    GyrX = data['GyrX']
    GyrY = data['GyrY']
    GyrZ = data['GyrZ']
    Alt = data['Alt']
    Temp = data['Temp']

    p011.set_data(index,AccX)
    p012.set_data(index,AccY)
    p013.set_data(index,AccZ)
    
    p021.set_data(index,MagX)
    p022.set_data(index,MagY)
    p023.set_data(index,MagZ)
    
    p031.set_data(index,Alt)
    p041.set_data(index,Temp)

    p051.set_data(index,GyrX)
    p052.set_data(index,GyrY)
    p053.set_data(index,GyrZ)

    n=len(index)
    if n>xmax:
        a=n-xmax
    else:
        a=0

    p011.axes.set_xlim(a,n)
    p021.axes.set_xlim(a,n)
    p031.axes.set_xlim(a,n)
    p041.axes.set_xlim(a,n)
    p051.axes.set_xlim(a,n)

    Acc=[AccX[a:n].max(),AccY[a:n].max(),AccZ[a:n].max(),AccX[a:n].min(),AccY[a:n].min(),AccZ[a:n].min()]
    Mag=[MagX[a:n].max(),MagY[a:n].max(),MagZ[a:n].max(),MagX[a:n].min(),MagY[a:n].min(),MagZ[a:n].min()]
    Alti=[Alt[a:n].max(),Alt[a:n].min()]
    Tempo=[Temp[a:n].max(),Temp[a:n].min()]
    Gyro=[GyrX[a:n].max(),GyrY[a:n].max(),GyrZ[a:n].max(),GyrX[a:n].min(),GyrY[a:n].min(),GyrZ[a:n].min()]

    p011.axes.set_ylim(min(Acc)-2,max(Acc)+2)
    p021.axes.set_ylim(min(Mag)-5,max(Mag)+5)
    p031.axes.set_ylim(min(Alti)-2,max(Alti)+2)
    p041.axes.set_ylim(min(Tempo)-2,max(Tempo)+2)
    p051.axes.set_ylim(min(Gyro)-5,max(Gyro)+5)

    # Writing the figure to streamlit canvas
    placeholder.write(f0)
    # return p011, p012, p013, p021, p022, p023, p031, p041, p051, p052, p053

# interval: draw new frame every 'interval' ms
# frames: number of frames to draw
#simulation = animation.FuncAnimation(f0, updateData, blit=False,  interval=20, repeat=False)



# Uncomment the next line if you want to save the animation
#simulation.save(filename='sim.mp4',fps=30,dpi=300)

#plt.show()


if start_button.button('Start', key='start'):
    start_button.empty()

    if st.button('Stop', key='stop'):
        pass
    while True:
        updateData()
        time.sleep(0.1)