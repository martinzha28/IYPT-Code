import math

def indexOfRefraction(depth):
    return(13.04*depth*depth + 0.1667*depth) + 1.3474
    
depthIncrement = 0.0001 #the dy value increment of 0.1 mm
depth = -0.0714 # down is negative 
angle = math.radians(92) # angle with vertical
totalRange = 0 # right is positive

maxDepth = -0.15

totalRangeArray = []

print("Test")
for i in range (1, 150):
    depth= -i/1000
    while (depth > maxDepth):   #arbitrary value
        totalRange += (depthIncrement * math.tan(angle))
        angle = math.asin(((indexOfRefraction(depth + depthIncrement)) / indexOfRefraction(depth)) * math.sin(angle))
        depth -= depthIncrement
        totalRangeArray.append(totalRange)
        
    outputdepth = 0.15+(-i/1000)
    outputheight = 15- outputdepth * 100

    
    print(outputheight, "  ",totalRangeArray[(i-1)]*1000,)   #round(depth, 7)
  
indexOfRefraction(depth) #Calls the functions 
