import math
import matplotlib.pyplot as plt

#slope angle (determines coupling) THE NEXT THREE YOU CAN TOUCH 
n = 28
L = 1
R = 0.03


#mass and moment of inertia THESE TWO YOU CAN TOUCH
m = 0.2
I = 0.0002
#spring constant and torsional spring constant THESE TWO YOU CAN TOUCH
k = 2
d = 0.013

#initial position and velocity up-down and spinny (from equilibrium) THESE FOUR YOU CAN TOUCH
z = 0.1
theta = 0
theta_vel = 0
z_vel = 0

#dont touch these
alpha = math.degrees(math.asin((L)/(n*2*math.pi*R)))
s = math.sin(math.radians(alpha))
c = math.cos(math.radians(alpha))
g = 9.8
z_vel = 0
theta_vel = 0
t = 0.0001
rep = 100000
zlist = []
thetalist = []
equi = -1*(m*g)/k
zpos = equi + z
zllist = []
thllist = []
z_accel = ((c*-1*k*zpos)/m) + ((s*theta*d)/(R*m))
theta_accel = ((c*-1*theta*d)/I) - ((s*k*zpos*R)/I)
long = k/m
tors = d/I
first = (c**2)*((long**2)+(tors**2)-(2*long*tors))
second = 4*(s**2)*tors*long
omegaf = math.sqrt(((c*(long+tors))+math.sqrt(first + second))/2)
omegas = math.sqrt(((c*(long+tors))-math.sqrt(first + second))/2)
B = 0
C = (((s*d*z)/(I*R))+((theta*c*d)/(I))-((theta)*(omegaf**2)))/((omegas**2)-(omegaf**2))
A = theta - C
D = (((s*d*z_vel)/(I*R))+((theta_vel*c*d)/(I))-((theta_vel)*(omegaf**3)))/((omegas**3)-(omegaf**3))

tplaylist = []
zplaylist = []
alphaplaylist = []

#begin loop
for i in range(0, rep):
    alpha = math.degrees(math.asin((L+z)/(n*2*math.pi*R)))
    s = math.sin(math.radians(alpha))
    c = math.cos(math.radians(alpha))
    alphaplaylist.append(alpha)
    zlist.append(z)
    thetalist.append(theta)
    z_accel = -1*(k/m)*(c*z+(s*R*theta))
    theta_accel = -1*(d/I)*(c*theta+((s*z)/R))
    z_vel += z_accel*t
    theta_vel += theta_accel*t
    z += z_vel*t
    theta += theta_vel*t
    time = i*t
    curthet = (A*math.cos(omegaf*time))+(B*math.sin(omegaf*time))+(C*math.cos(omegas*time))+(D*math.sin(omegas*time))
    curthetdevdev = (-1*(omegaf**2)*A*math.cos(omegaf*time)) + (-1*(omegaf**2)*B*math.sin(omegaf*time)) + (-1*(omegas**2)*C*math.cos(omegas*time)) + (-1*(omegas**2)*D*math.sin(omegas*time))
    curz = (-1*(((curthetdevdev*I*R))/(s*d))) + (-1*(((curthet*c*R))/(s)))
    tplaylist.append(curthet)
    zplaylist.append(curz)

fig, axs = plt.subplots(5)
fig.suptitle('plots')
#the things that matter are plotted ordered as: real values of z, theta, and then theoretical values of z, theta
axs[0].plot(zlist)
axs[1].plot(thetalist)
axs[2].plot(zplaylist)
axs[3].plot(tplaylist)
#this last plot was just for testing, ignore it for now
axs[4].plot(alphaplaylist)
plt.show()
