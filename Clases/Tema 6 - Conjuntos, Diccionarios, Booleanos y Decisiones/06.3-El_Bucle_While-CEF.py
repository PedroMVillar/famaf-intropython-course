#!/usr/bin/env python
# coding: utf-8

# ![Header_CursoBasico.png](attachment:6594ce06-1e81-4e55-ae39-cd96c5fff0b6.png)

# # El bucle `while`

# ### Sintaxis

# ```python
# while condicion:
#     bloque de enunciado```
# - El bucle `while`  es un bucle indefinido. El número de iteraciones no se conoce hasta que el ciclo haya finalizado.

# ### Ejemplos

# ```python
# for i in range(5):
#     print(i)```

# - El bucle while equivalente es el siguiente:

# In[1]:


i = 0
while i < 5:
    print(i)
    i += 1


# - El siguiente código conducirá a un bucle infinito o infinito: 
# ## No lo corra

# In[2]:


i = 0
while i < 5:
    print(i)


# - Para forzar la terminación del código, puede intentar lo siguiente:
# 
#     - Haga clic en el menú de Jupyter Notebook "Kernel / Reiniciar".
#     
#     - Si no funciona, presione CTRL + C varias veces en el terminal para interrumpir el servidor Jupyter Notebook conectado.
# 
#     - Si el navegador no responde, intente abrir el Administrador de tareas usando CTRL + ALT + SUPR y elimine el programa del navegador.
#     
#     - Si su computadora se congela, desconecte la alimentación y retire la batería.
#     
#     - Si su computadora continúa, corra!

# In[2]:


i = 0
Condicion = True
while Condicion:
    print(i)
    i += 1
    if i == 5:
        Condicion = False


# ### Bucle interactivo

# - Este ejemplo pregunta si el usuario necesita ingresar más datos durante cada iteración del ciclo.

# In[3]:


def main():
    k = 0
    total = 0.0
    more = "si"
    while more[0] == "s" or more[0] == "S":
        num = float(input("Ingrese un número: "))
        k += 1
        total += num
        more = input("¿Más números? s/n?")
    avg = total / k
    print()
    print('Ingresaste', k, 'numeros.')
    print('El total es', total)
    print("El promedio es", avg)

main()


# ### El Loop centinela

# - El centinela es la condición que señala el final del bucle.
# 
# - En el siguiente ejemplo, calculamos el promedio de puntajes de prueba ingresados ​​por el usuario.
# 
# - Si una entrada está fuera del rango [0, 100], el bucle se detiene.

# In[4]:


def main():
    k = 0
    total = 0.0
    num = float(input("Ingrese un número entre 0 y 100 (otros para salir): "))
    while 0 <= num <= 100:  # num is the test score
        k += 1
        total += num
        num = float(input("Ingrese un número entre 0 y 100 (otros para salir): "))
    avg = total / k
    print()
    print('Ingresó ', k, 'números entre 0 y 100.')
    print('El total es', total)
    print("El promedio es", avg)

main()


# - Si los números pueden tomar valores positivos y negativos (por ejemplo, temperatura), podemos usar un carácter especial como 'q' (salir), 'e' (salir) o incluso '' (vacío) para señalar el final de el lazo.

# In[6]:


def main():
    k = 0
    total = 0.0
    string = input("Ingrese un número (presione ENTER para salir): ")
    while string != "":
        num = float(string)
        k += 1
        total += num
        string = input("Ingrese un número (presione ENTER para salir): ")
    avg = total / k
    print()
    print('Ingresaste', k, 'números.')
    print('El total es', total)
    print("El promedio es", avg)

main()


#  
