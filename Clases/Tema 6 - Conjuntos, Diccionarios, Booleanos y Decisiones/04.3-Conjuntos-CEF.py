#!/usr/bin/env python
# coding: utf-8

# ![Header.png](attachment:Header.png)

# # Conjuntos

# ### Lo Básico

# - Los conjuntos contienen colecciones desordenadas de elementos únicos.
# - Los conjuntos se indican con llaves. 
# - Contienen elementos en lugar de clave: pares de valores.

# In[1]:


d = {'apples':33, 'bananas':47, 'oranges':27}
type(d)


# In[2]:


s = {'apples', 'bananas', 3.14, -5}
type(s)


# In[3]:


3 in s


# In[4]:


'apples' in s


# In[5]:


s = set([1, 2, 1, 3, 4, 4])
s


# In[6]:


len(s)


# - Los conjuntos no admiten indexación, segmentación u otro comportamiento similar a la secuencia.

# In[7]:


s


# In[8]:


s[2]


# ### Los conjuntos son mutables

# In[9]:


s = {}  # Crea un diccionario vacío, no un conjunto
s


# In[10]:


type(s)


# In[11]:


s = set()  # Un conjunto vacío
s


# In[12]:


type(s)


# In[13]:


s.add(4)
s


# In[14]:


s = set((1, 2, 3)) # Crear un conjunto de una lista o tupla
s


# In[15]:


s.add('Hola Mundo')
s


# ### Operaciones de Conjuntos

# In[16]:


s1 = {1, 2, 3}
s2 = {1, 3, 4}
s1 | s2  # Union de conjuntos


# In[17]:


s1 = {1, 2, 3}
s2 = {1, 3, 4}
s1 & s2  # Interseccion de conjuntos


# In[18]:


s1 = {1, 2, 3}
s2 = {1, 3, 4}
s1 - s2  # Diferencia de conjuntos


# In[19]:


s2 - s1  # Diferencia de conjuntos


# In[20]:


s1 = {1, 2, 3}
s2 = {1, 3, 4}
s1 ^ s2  # Diferencia simétrica


# In[21]:


s1 = {1, 2, 3}
s2 = {1, 3, 4}
s1 <= s2  # Subsets: s1 ⊆ s2? 


# In[22]:


s2 <= s1  # Subsets: s2 ⊆ s1? 


# In[23]:


s1 = {1, 2, 3}
s3 = {1, 2}
s1 > s3   # s1 ⊃ s3?


# ### Ejemplo: empleados

# In[24]:


fisicos = {'Jane', 'Jack', 'Julie'}
programadores = {'Jack', 'Sam', 'Susan'}
matematicos = {'Jane', 'Susan', 'Zack'}


# In[25]:


todosempleados = fisicos | programadores | matematicos
todosempleados


# In[26]:


fisic_matemat = fisicos & matematicos
fisic_matemat


# In[27]:


fulltime_matematicos = matematicos - fisicos - programadores
fulltime_matematicos


# In[28]:


fisicos.add('Mark')  #Se une Mark
fisicos


# In[29]:


todosempleados.add('Mark')
todosempleados


# In[30]:


for group in [fisicos, programadores, matematicos, todosempleados]:
    group.discard('Susan')   #Se va Susan
    print(group)


# In[ ]:




