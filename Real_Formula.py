import math

line = float(input())
leg = float(input())

ans = ((16*((math.sin(math.atan(line/(leg+0.4))+(math.pi/6))+1/4)**2)+3)**0.5)/(2*(3**0.5))

print("index of reflection : %0.5f"%ans)
