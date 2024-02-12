#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
numero_entero = 5
if numero_entero > 0:
    print("El número es mayor que cero")
elif numero_entero < 0:
    print("El número es menor que cero")
else:
    print("El número es igual a cero")




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:


variable1 = 5
variable2 = "Hola"

if type(variable1) == type(variable2):
    print("Las variables son del mismo tipo de dato")
else:
    print("Las variables son de tipos diferentes")


# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(1, 21):
    if i % 2 == 0:
        print("{i} es un número par")
    else:
        print("{i} es un número impar")



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(6):
    resultado = i ** 3
    print("{i} elevado a la potencia de 3 es igual a {resultado}")

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

numero_entero = 4

for _ in range(numero_entero):
    print("Este es un ciclo del bucle")



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

numero = 5

if isinstance(numero, int) and numero > 0:
    factorial = 1
    i = 1

    while i <= numero:
        factorial *= i
        i += 1
    print("El factorial de {numero} es: {factorial}")
else:
    print("La variable no contiene un número entero mayor que 0")



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

contador = 0

while contador < 3:
    print("Este es el ciclo while, iteración {contador + 1}:")
    
    for i in range(1, 4):
        print("Este es el ciclo for, iteración {i}")
    
    contador += 1



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

for i in range(1, 4):
    print("Este es el ciclo for, iteración {i}:")
    
    j = 1
    while j <= i:
        print("Este es el ciclo while, iteración {j}")
        j += 1





# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# números primos entre 0 y 30
print("Números primos entre 0 y 30:")
for num in range(31):
    if es_primo(num):



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

print("Números primos entre 0 y 30:")
for num in range(2, 31):
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

#La optimización se logró al utilizar la sentencia break para salir del bucle pronto 
#como se encuentra un divisor en el segundo insciso (punto 10). 
#Esto reduce la cantidad de iteraciones necesarias para verificar la 
#primalidad de un número, mejora la eficiencia del código. 
#La optimización podría variar dependiendo del rango de números evaluados
#y podría ser más notable para números más grandes.



# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

numero = 100

while numero <= 300:
  
    if numero % 12 != 0:
        numero += 1
        continue

    print(numero)
    numero += 1



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# buscar números primos
def buscar_primo():
    while True:

        entrada = input("Ingresa un número entero mayor que 1 para verificar si es primo (o 'salir' para terminar): ")
        
        if entrada.lower() == 'salir':
            print("Saliendo...")
            break
        
        # Convertir la entrada en entero
        try:
            numero = int(entrada)
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
            continue
        
        # Verificar si el número es primo y dar resultado
        if numero > 1:
            if es_primo(numero):
                print(f"{numero} es un número primo.")
            else:
                print(f"{numero} no es un número primo.")
        else:
            print("Por favor, ingresa un número entero mayor que 1.")

# Llamar a la función 
buscar_primo()


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

numero = 100

# Buscar el primer número divisible por 3 y múltiplo de 6
while numero <= 300:
    if numero % 3 == 0 and numero % 6 == 0:
        print(f"El primer número divisible por 3 y múltiplo de 6 dentro del rango es: {numero}")
        break
    numero += 1
else:
    print("No se encontró ningún número que cumpla con las condiciones dentro del rango.")

