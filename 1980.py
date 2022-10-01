print("-------------------------------------------------------")
print("--------Calcular la rata de una población--------------")
print("-------------------------------------------------------")

#INPUT
A = 3.5 
B = 5.0
N = 1980  

#PROCESS
while A<B:
    A = A+0.07*A 
    B = B+0.05*B 
    N = N+1 

#OUTPUT
print("El crecimiento de la población A\nEs mayor que la población B en el año: " + str(N))