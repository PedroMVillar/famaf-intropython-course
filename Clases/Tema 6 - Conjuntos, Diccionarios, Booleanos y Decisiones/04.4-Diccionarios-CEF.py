#!/usr/bin/env python
# coding: utf-8

# ![Header.png](attachment:Header.png)

# # Dictionaries

# ### Lo Básico

# - Un diccionario representa una lista de claves: pares de valores contenidos entre llaves, {}.

# In[1]:


inventario = {'apples': 430, 'bananas': 312, 'oranges': 525}
inventario


# In[2]:


type(inventario)


# In[3]:


inventario['bananas']  # Indexing


# In[4]:


len(inventario)


# In[5]:


'apples' in inventario


# In[6]:


'blueberries' not in inventario


# - Las claves deben ser únicas dentro de un diccionario.

# In[7]:


inventario = {'apples': 430, 'apples': 312, 'oranges': 525}
inventario


# - La clave: los pares de valores no están ordenados.

# In[8]:


kids = {'Emma': 14, 'Tom': 10, 'Jacob': 8}
kids


# In[9]:


kids = dict([('Emma', 14), ('Tom', 10), ('Jacob', 8)])
kids


# In[10]:


kids.keys()


# In[11]:


list(kids.keys())  # Devuelve una lista de todas las claves utilizadas en el diccionario, en orden arbitrario


# In[12]:


sorted(kids.keys())  # Lista ordenada de todas las claves utilizadas en el diccionario.


# In[13]:


kids.values()


# In[14]:


kids.items()  # Devuelve una lista de pares de tuplas de diccionario (clave, valor)


# In[15]:


for name, age in kids.items():
    print(name, age)


# - Cuando las claves son cadenas simples, podemos especificar pares usando argumentos de palabras clave:

# In[16]:


spanish = dict(hello='hola', yes='si')
spanish


# In[17]:


spanish = dict('hello'='hola', 'yes'='si')  # Esto está mal


# ### Los diccionarios son mutables

# In[18]:


inventario = {'apples': 430, 'bananas': 312, 'oranges': 525}
inventario


# In[19]:


del inventario['bananas']
inventario


# In[20]:


inventario['oranges'] = 0
inventario


# In[21]:


spanish = {}  # Diccionario vacio
spanish


# In[22]:


spanish = dict()  # Diccionario vacio
spanish


# In[23]:


spanish['hello'] = 'hola'
spanish['yes'] = 'si'
spanish


# In[24]:


spanish.clear()  # Elimina todos los elementos.
spanish


# ### Comprensiones de diccionario

# - La comprensión de diccionario se pueden usar para crear diccionarios a partir de expresiones de valores y claves arbitrarias.

# In[25]:


squares = {x: x**2 for x in (2, 4, 6)}
squares


# - Es equivalente a:

# In[26]:


squares = dict()
for x in (2, 4, 6):
    squares[x] = x**2
squares


# In[ ]:





# In[ ]:




