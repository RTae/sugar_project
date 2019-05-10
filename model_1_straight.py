import math
reflec_index = [1.33, 1.34026 ,1.34782, 1.35568, 1.36384, 1.37233, 1.38115, 1.39032, 1.39986, 1.40987, 1.42009, 1.4308, 1.44193]

for i in range(len(reflec_index)) :
    seta = math.degrees(math.asin((math.sin(math.radians(30)))*reflec_index[i]))

    print("Brix degree : "+ str(i*5) +" reflec_index : " + str(reflec_index[i]) + " Degrees : " +str(seta)+" degree")
