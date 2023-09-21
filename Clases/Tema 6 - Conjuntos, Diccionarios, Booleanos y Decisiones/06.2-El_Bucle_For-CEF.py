#!/usr/bin/env python
# coding: utf-8

# ![Header_CursoBasico.png](attachment:614febeb-9d33-487c-b472-3babe729415d.png)

# # El Loop `for`

# ### Syntaxis

# ```python
# for item in sequence:
#     statement block```
# 
# - El `for` El bucle es un bucle definido. El número de iteraciones se determina antes de que comience el ciclo.

# ### Examples

# In[1]:


for letter in 'Hola':
    print(letter)


# In[2]:


colors = ['red', 'green', 'blue']
for color in colors:
    print('Current color:', color)


# In[3]:


import math
for x in range(0, 3):
    print('x =', x)
    print('sin(x) =', math.sin(x))
    print()


# In[7]:


help(math.sin)


# In[14]:


lists = [[3.14], ['Apple', 'Orange'], [3, 4, 5]]
for sublist in lists:
    for x in sublist:  # Nested loop
        print(x)


# In[15]:


def main():
    k = int(input('Ingrese el valor de k: '))
    total = 0.0
    for i in range(k):
        num = float(input('Ingrese un numero: '))
        total += num
    avg = total / k
    print()
    print('Ingresaste', k, 'numbers.')
    print('El total es', total)
    print("El promedio es", avg)

main()


# ### Recorriendo archivos

# - El siguiente programa calcula el promedio de todos los 30 números en el `data1.txt` archivo. 
# - Cada línea contiene como máximo un número. Algunas líneas están vacías.

# In[18]:


def main():
    k = 0
    total = 0.0
    
    with open('data1.txt','r') as f:
        data = f.readlines()  # Leer todas las líneas a los datos
        print(data)
        
        for num in data:
            if num !='\n':  # Excluyendo las líneas vacías
                k += 1
                total += float(num)
    
    avg = total / k
    print()
    print(k, 'los números fueron leídos del archivo.')
    print('El total es', total)
    print("El promedio es", avg)

main()


# - El siguiente programa calcula el promedio de todos los 30 números en el `data2.txt` archivo.
# - Cada línea puede contener uno o más números, separados por una coma y un espacio (', '). 
# - Algunas lineas estan vacias.

# In[19]:


def main():
    k = 0
    total = 0.0
    
    with open('data2.txt','r') as f:
        data = f.readlines()  # Leer todas las líneas a los datos
        print(data)
        
        # Este es un bucle anidado
        for line in data:  # Procesar cada línea en el archivo
            for num in line.split(', '):  # Procesar cada número en la línea.
                if num !='\n':  # Excluyendo las líneas vacías
                    k += 1
                    total += float(num)
    
    avg = total / k
    print()
    print(k, 'números se leyeron del archivo.')
    print('El total es', total)
    print("El promedio es", avg)

main()


# In[24]:


for ii in range(2, 15, 2):
    print(ii)


# In[25]:


for ii in range(20,5,-2):
    print(ii)


# In[ ]:




