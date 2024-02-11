#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

numero_entero = 42
print("El número entero es:", numero_entero)


# 2) Imprimir el tipo de dato de la constante 8.5

print(type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(numero_entero))



# 4) Crear una variable que contenga tu nombre

# In[2]:

nombre = "Luz"


# 5) Crear una variable que contenga un número complejo

# In[3]:

numero_complejo = 3 + 4j



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:


print(type(numero_complejo))


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
import math

pi_redondeado = round(math.pi, 4)
print(pi_redondeado)

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
valor_string = 'True'
valor_booleano = True
print(valor_string == valor_booleano)


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(valor_string))
print(type(valor_booleano))

# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

numero_entero = 10
numero_decimal = 3.5

resultado = numero_entero + numero_decimal

print("El resultado de la suma es:", resultado)



# 11) Realizar una operación de suma de números complejos

# In[2]:

complejo_1 = 2 + 3j
complejo_2 = 1 - 2j

resultado = complejo_1 + complejo_2

print("El resultado de la suma es:", resultado)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:


numero_real = 5
numero_complejo = 3 + 2j

resultado = numero_real + numero_complejo
print("El resultado de la suma es:", resultado)


# 13) Realizar una operación de multiplicación

# In[5]:


numero_real_1 = 5
numero_real_2 = 3.5

resultado = numero_real_1 * numero_real_2

print("El resultado de la multiplicación es:", resultado)


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
resultado = 2 ** 8

print("El resultado de 2 elevado a la octava potencia es:", resultado)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

cociente = 27 // 4
print("El cociente de la división de 27 entre 4 es:", cociente)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

parte_entera = 27 // 4
print("La parte entera de la división de 27 entre 4 es:", parte_entera)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

resto = 27 % 4
print("El resto de la división de 27 entre 4 es:", resto)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

parte_entera = 27 // 4
resto = 27 % 4
resultado = parte_entera * 4 + resto
print("El resultado es:", resultado)




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

variable1 = "Hola"
variable2 = " mundo"

resultado = variable1 + variable2

print(resultado)



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

if int("2") == 2:
    print("La comparación es verdadera")
else:
    print("La comparación es falsa")



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:


if "2" == str(2):
    print("La comparación es verdadera")
else:
    print("La comparación es falsa")


# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

a = float('3.8')
print(a)

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
variable = 3
variable -= 1

print(variable)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

#1 << 2 = 0100

#0100 = 4 
#porque es un número binario




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:


#No se puede sumar un numero entero con un texto, porque el 2 está entre comillas simples.



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:


numero_entero = 10
cadena_texto = "El número es: "

resultado = cadena_texto + str(numero_entero)

print(resultado)
