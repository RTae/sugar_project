import math
reflec_index = [1.33, 1.34026 ,1.34782, 1.35568, 1.36384, 1.37233, 1.38115, 1.39032, 1.39986, 1.40987, 1.42009, 1.4308, 1.44193]
leg = []
error = 0

lenght = float(input("Length : "))

for i in range(len(reflec_index)) :
    seta_2 = math.degrees(math.asin((math.sin(math.radians(30)))/reflec_index[i]))
    seta_3 = 90 - (180 - (30-seta_2 + 120))
    seta_4 = math.degrees(math.asin((math.sin(math.radians(seta_3)))*reflec_index[i]))
    line = math.tan(math.radians(seta_4)) * (lenght)
    leg.append(round(seta_3, 3))

    if i > 0 :
        seta_deta = leg[i] - leg[0]
        error = (2.4*math.sin(math.radians(seta_deta)))/math.sin(math.radians(90-leg[i]))

    print(" ")
    print("Error : %f" %error)
    print("input_degree_2 : %0.3f" %seta_2)
    print("input_degree_3 : %0.3f" %seta_3)
    print("Brix degree : "+ str(i*5) +", reflec_index : " + str(reflec_index[i]) + ", Degrees : %0.3f degree " %seta_4 + ", Range : %0.3f cm" %line  )

    y = math.radians(seta_4)
    ans = ((16*((math.sin(y)+1/4)**2)+3)**0.5)/(2*(3**0.5))
    print("index of reflection : %0.5f"%ans)
