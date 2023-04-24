print("--------------------------------------------------")
print("-------------TABLA DE MULTIPLICAR-----------------")
print("--------------------------------------------------")



def Generar_tabla_multiplicar (n):
    print("Tabla del " + str(n))
    for i in range (1,11):
       print(str(n) + " X " + str(i) + " = " + str(n * i))
       
    
    
n = int(input("Digite el numero de la tabla de multiplicar: "))
Generar_tabla_multiplicar(n)

    
 










 
