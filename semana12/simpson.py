def chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)] 
  

def SimpsonCalculation38(h, x0, x1, x2, x3 ): 
    integral =  (3 * h / 8) * (x0 + (3 * x1) + (3 * x2) + x3 ) 
    return integral

def SimpsonCalculation13(h, x0,x1,x2):
    integral =  (h/3) * (x0 + (4 * x1) +x2)
    return integral
    
x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9]
y = [0.269,2.294,6.479,12.824,21.329,31.994,44.819,59.804,76.949,96.254,117.719,141.344,167.129,195.074,225.179,257.444,291.869,328.454,367.199]

x = chunks(x,4)
y = chunks(y,4)
h = 0.5

total = 0

for i in range(len(x)):
    x_temp = x[i]
    y_temp = y[i]

    if(len(x_temp) == 4):
        total = total + SimpsonCalculation38(h, y_temp[0],y_temp[1],y_temp[2],y_temp[3])
    elif (len(x_temp) == 3):
        total = total + SimpsonCalculation13(h, y_temp[0],y_temp[1],y_temp[2])
    

print(total)


  