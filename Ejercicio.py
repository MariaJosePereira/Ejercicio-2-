
# Online Python - IDE, Editor, Compiler, Interpreter
"""Ejercicio 2"""
#Funciones
def load_values(values):
    follow=1
    while follow==1:
        values.append(int(input("Enter the values: ")))
        follow=int(input("Enter 1 to make another record of values: "))
        
def calculate_average(lista):
    return sum(lista)/len(lista)
    
def calculate_median(lista):
    lista.sort()
    totalElem=len(lista)
    if (totalElem%2!=0):
        median=lista[totalElem//2]
    else:
        a = lista[totalElem//2]
        b = lista[totalElem//2-1]
        median=(a+b)/2-1
    return median
    
def mode(lista):
    contRep=0
    major=0
    tamLista=len(lista)
    for valueA in range(tamLista):
        contRep=0
        for valueB in range(tamLista):
            if(lista[valueA]==lista[valueB]):
                contRep+=1
        if(contRep>major):
            major=contRep
            mode=lista[valueA]
    return mode
    
def standard_deviation(lista):
    S=0
    N=len(lista)
    S1=0
    for i in range(0,N):
        S=S+lista[i] 
    average=S/N
    print("average: ",average)
    for j in range(0,N):
        S1=S1+(lista[j]-average)*(lista[j]-average)
    vari=S1/N 
    standard=(vari)**(1/2)
    print("variance: ",vari)
    print("standard deviation:",standard)
    
#Inicio 
values=[]
load_values(values)

#Final 
print("")
print("Statistics")
print("****************")
print("Total recorded values: ",len(values))
print("The average of the values is: ",round(calculate_average(values),2))
print("The median of the values is: ",calculate_median(values))
print("The mode of the entered values is: ",mode(values))
print("the standard deviation of the input values is: ",standard_deviation(values))
print("")



    
  
    
