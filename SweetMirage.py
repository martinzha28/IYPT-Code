import math
import array as arr
import matplotlib.pyplot as plt

# Real tank size is: 7.62 cm * 45.72 cm * 20.32 cm (3 x 18 x 8 inch)
# Each layer of sugar water is: 500 ml, (total 5 layers)

nwater = 1.33299 # Water index at 20 degree
n80p = 1.48559 # 80% Sugar water reflactive index at 20 degree: 1.49
input_angle = 75 # input light ray angle in degree
pi314 = (math.pi)
Height = 5 * 500 / 7.5 / 45.72 # Total sugar solution height in the tank
dy = 0.1 # cm of the minium unit of layer
nloop = int(round(Height/dy, 0)) # Total looping cycles, round to integer
totalxa1 = 0 # Start from x=0
Snell_value = n80p * math.sin(input_angle * pi314 / 180) # switch to Radian and calculate sinQ * n80p
indexn = []   # Array for each water layer of index
xleveln = []  # Array for each layer of light ray travels
anglen = []   # Array for input angle of each layer
totalx = []   # Array for x axis number for draw
totaly = []   # Array for y axis number for draw
Loop_counter = 0 
drawx = []    
drawy = []


for x in range(0, nloop):
    a1 = x * dy
    Loop_counter = x
    totaly.append(a1)
    indexa1 = n80p - (n80p - nwater) / Height * x * dy
    indexn.append(indexa1)

    if Snell_value / indexa1 > 1:

        break

    anglena1 = math.asin(Snell_value / indexa1)

    anglen.append(anglena1)
    xlevelna1 = math.tan(anglena1) * dy
    xleveln.append(xlevelna1)
    totalxa1 = totalxa1 + xlevelna1
    totalx.append(totalxa1)

    if totalxa1 > 45.72:

        break

    

# Draw the curve

print('Loop_counter = ', Loop_counter)

from pylab import *

for x in range(0, 2 * Loop_counter - 1):
    if x < Loop_counter:
        drawx.append(round(totalx[x],3))
        drawy.append(round(totaly[x],2))
        print('drawx[',x,'] = ', drawx[x], ';    drawy[',x,'] = ', drawy[x])

    else:

        # once total reflection happens, symetry the values

        drawx.append(round(2 * drawx[Loop_counter - 1] - totalx[2 * Loop_counter - x - 2],3))
        drawy.append(round(totaly[2 * Loop_counter - x - 2],2))
        print('drawx[',x,'] = ', drawx[x], 'drawy[',x,'] = ', drawy[x])

plot(drawx, drawy, color = 'red')

#plt.ylim(1,8)

#plt.xlim(1,46)

plt.xlabel('Tank Length (cm)')
plt.ylabel('Tank Height (cm)')
plt.title('Fata Morgana Light Ray Simulate Chart')
plt.grid(True)
plt.show()
