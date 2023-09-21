#!/usr/bin/env python
# coding: utf-8

# ![Header_CursoBasico.png](attachment:866e7276-83a4-454c-9d95-a16bf7048cfb.png)

# # Control de decisiones

# ###  La declaración de `if`

# **Syntaxis**

# - El bloque de instrucciones está sangrado. Se ejecutará solo si `condition` es `True`.
# ```python
#     if condition:
#         bloque de enunciado
# ```

# **Ejemplo**

# - El siguiente programa convierte la velocidad de un automóvil de kilómetros por hora (kph) a millas por hora (mph).
# - Se emitirán advertencias si el automóvil es demasiado rápido o demasiado lento

# In[1]:


def speed1():
    kph = float(input('¿Cuál es la velocidad en km / h?'))
    mph = 0.621371 * kph
    print('La velocidad es de', mph, 'mph.')

    if mph > 65:
        print('Está por encima del límite de velocidad (65 mph). ¡Maneja más despacio!')
    if mph <= 65:
        print('Estás dentro del límite de velocidad. ¡Buen trabajo!')


# In[2]:


speed1()


# In[3]:


speed1()


# ### La declaración `if-else`

# **Syntaxis**

# - El `bloque de enunciado_1` se ejecutará si la condición es `True`;
# - De lo contrario, `bloque de enunciado_2` se ejecutará.
# ```python
# if condition:
#     statement_block_1
# else:
#     statement_block_2```

# **Ejemplo**

# In[4]:


def speed2():
    kph = float(input('¿Cuál es la velocidad en km / h?  '))
    mph = 0.621371 * kph
    print('La velocidad es ', mph, 'mph.')

    if mph > 65:
        print('Está por encima del límite de velocidad (65 mph). ¡Maneja más despacio!')
    else:
        print('Estás dentro del límite de velocidad. ¡Buen trabajo!')


# In[5]:


speed2()


# In[6]:


speed2()


# ### La declaración `if-elif-else`

# **Syntaxis**

# - Python evalúa cada condición en orden, buscando la primera que sea `True`.
# - Si se encuentra una condición `True`, se ejecutará el bloque de instrucción correspondiente.
# - Si ninguna de las condiciones es `True`, se ejecutará el `else` con el último`statement_block_n`.
# 
# ```python
# if condition_1:
#     statement_block_1
# elif condition_2:
#     statement_block_2
# elif condition_3:
#     statement_block_3
# ...
# else:
#     statement_block_n
# ```

# **Ejemplo**

# In[4]:


def speed3():
    kph = float(input('¿Cuál es la velocidad en km / h?'))
    mph = 0.621371 * kph
    print('La velocidad es de', mph, 'mph.')
    
    if mph > 80:
        print('Estás MUY por encima del límite de velocidad. ¡Tu multa es de $ 200!')
    elif 65 < mph <= 80:
        print('Está por encima del límite de velocidad (65 mph). ¡Maneja más despacio!')
    elif 30 <= mph <=65:
        print('Estás dentro del límite de velocidad. ¡Buen trabajo!')
    else:
        print('Eres muy lento. ¡Sal de la autopista y usa las carreteras locales!')


# In[5]:


speed3()


# In[6]:


speed3()


# In[10]:


speed3()


# In[11]:


speed3()


# In[ ]:




