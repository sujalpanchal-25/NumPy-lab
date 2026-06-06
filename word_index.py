import numpy as np

arr = np.array([[['A' , 'B' , 'C'] , ['D' , 'E', 'F'] , ['G' , 'H' , 'I']],
               [['J' , 'K' , 'L'] , ['M' , 'N', 'O'] , ['P' , 'Q' , 'R']],
               [['S' , 'T' , 'U'] , ['V' , 'W', 'X'] , ['Y' , 'Z' , ' ']]])

F_name = arr[2,0,0] + arr[2,0,2] + arr[1,0,0] + arr[0,0,0] + arr[1,0,2]
L_name = arr[1,2,0] + arr[0,0,0] + arr[1,1,1] + arr[0,0,2] + arr[0,2,1] + arr[0,0,0] + arr[1,0,2]
print(F_name + " " +  L_name)