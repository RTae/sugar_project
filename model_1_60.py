import math
reflec_index = [1.33, 1.34026 ,1.34782, 1.35568, 1.36384, 1.37233, 1.38115, 1.39032, 1.39986, 1.40987, 1.42009, 1.4308, 1.44193]
leg = []
error = 0
lenght = float(input("Length : "))

for i in range(len(reflec_index)) :
    seta_2 = math.degrees(math.asin((math.sin(math.radians(60)))/reflec_index[i]))
    seta_3 = 60-seta_2
    seta_4 = math.degrees(math.asin((math.sin(math.radians(seta_3)))*reflec_index[i]))
    line = math.tan(math.radians(seta_4)) * (lenght)
    leg.append(round(line, 3))

    print(" ")
    print("input_degree_2 : %0.3f" %seta_2)
    print("input_degree_3 : %0.3f" %seta_3)
    print("Brix degree : "+ str(i*5) +", reflec_index : " + str(reflec_index[i]) + ", Degrees : %0.3f degree " %seta_4 + ", Range : %0.3f cm" %line  )
