import math
reflec_index = [1.33, 1.34026 ,1.34782, 1.35568, 1.36384, 1.37233, 1.38115, 1.39032, 1.39986, 1.40987, 1.42009, 1.4308, 1.44193]
leg = []
error = 0

lenght = float(input("Length : "))

for i in range(len(reflec_index)) :
    seta_2 = math.degrees(math.asin((math.sin(math.radians(30)))/reflec_index[i]))
    seta_3 = 90 - (180 - (30-seta_2 + 120))
    seta_4 = math.degrees(math.asin((math.sin(math.radians(seta_3)))*reflec_index[i]))
    line = math.tan(math.radians(seta_4-30)) * (lenght+0.4)

    leg.append(round(line,1))

    print(" ")
    print("input_degree_2 : %0.3f" %seta_2)
    print("input_degree_3 : %0.3f" %seta_3)
    print("Brix degree : "+ str(i*5) +", reflec_index : " + str(reflec_index[i]) + ", Degrees : %0.4f degree " %seta_4 + ", Range : %0.4f cm" %line  )

    ans = ((16*((math.sin(math.atan(line/(lenght+0.4))+(math.pi/6))+1/4)**2)+3)**0.5)/(2*(3**0.5))
    print("index of reflection : %f"%ans)


    if i % 2 == 0 and i != 0 :
        print("Delta : %f "%(leg[i]-leg[i-2]))

print(leg)
