import math
import csv
reflec_index = [1.33, 1.34026 ,1.34782, 1.35568, 1.36384, 1.37233, 1.38115, 1.39032, 1.39986, 1.40987, 1.42009, 1.4308, 1.44193]

with open('Sugar_project_input_46.csv', mode='w') as csv_file:
    fieldnames = ['Brix','reflec_index','Seta_2', 'Seta_3', 'Seta_4']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(reflec_index)) :
        seta_2 = math.degrees(math.asin((math.sin(math.radians(46)))/reflec_index[i]))
        seta_3 = 90 - (180 - (46-seta_2 + 104))
        seta_4 = math.degrees(math.asin((math.sin(math.radians(seta_3)))*reflec_index[i]))


        print(" ")
        print("input_degree_2 : %0.3f" %seta_2)
        print("input_degree_3 : %0.3f" %seta_3)
        print("Brix degree : "+ str(i*5) +", reflec_index : " + str(reflec_index[i]) + ", Degrees : %0.2f degree " %seta_4)

        writer.writerow({'Brix': str(i*5), 'reflec_index': str(reflec_index[i]), 'Seta_2': str(round(seta_2,2)), 'Seta_3': str(round(seta_3,2)), 'Seta_4': str(round(seta_4,2))})
