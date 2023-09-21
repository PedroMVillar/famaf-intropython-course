#!/usr/bin/env python
# coding: utf-8

# ![Header_CursoBasico.png](attachment:ba0570fe-a243-4a5f-af89-638d780c8d5b.png)

# # Operaciones booleanas

# ### Comparación booleana simple

# - George Boole (1815-1864), Matemático inglés. <img src="images/george_boole.jpg" alt="George Boole" style="width: 150px;"/>

# - Una expresión booleana solo puede devolver `True` or `False`.
# - Operadores de comparación booleanos simples:
# 
# | Operador | Significado                 |
# |:---------|:------------------------|
# | <        | strictly less than      |
# | <=       | less than or equal      |
# | >        | strictly greater than   |
# | >=       | greater than or equal   |
# | ==       | equal                   |
# | !=       | not equal               |
# | is       | object identity         |
# | is not   | negated object identity |

# - Estos operadores tienen la misma prioridad.
# - Las comparaciones se pueden encadenar. `x < y <= z` es equivalente a `x < y and y <= z`.

# In[1]:


3 < 4


# In[2]:


4 * 3 < 4 + 3  # Equivalente a (4 * 3) < (4 + 3)


# - Las comparaciones de cadenas se basan en el orden de ASCII y Unicode subyacentes.

# In[3]:


"hello" == "hello"


# In[4]:


"hello" < "Hello"  # Las letras minúsculas van después de las mayúsculas


# - Los dos lados deben ser del mismo tipo de datos.

# In[5]:


'hello' < 256  # This will not work


# In[6]:


type(True)


# In[7]:


type(False)


# In[8]:


type(true)  # Caso equivocado


# In[9]:


type(false)  # Caso equivocado


# ### Operaciones And, Or, y Not 

# - Podemos ensamblar múltiples expresiones booleanas simples juntas para hacer una expresión booleana compleja. 
# - La operación `and` de dos variables booleanas `x` y `y` es `True` solo si ambos `x` y `y` son `True`.
# 
# | x     | y     | x $y$ y |
# |:-----:|:-----:|:-------:|
# | True  | True  | True    |
# | True  | False | False   |
# | False | True  | False   |
# | False | False | False   |

# - La operación `or` de dos variables booleanas `x` and `y` is `True` cuando cualquiera `x` o `y` es `True`.
# 
# | x     | y     | x o y |
# |:-----:|:-----:|:------:|
# | True  | True  | True   |
# | True  | False | True   |
# | False | True  | True   |
# | False | False | False  |

# - `not` es el operador negación.
# 
# | x     | not x |
# |:-----:|:-----:|
# | True  | False |
# | False | True  |

# In[10]:


x = True
x = not x
x


# In[11]:


y = 3 <= 5  # Equivalente a y = (3 <= 5)
y


# In[12]:


x and y


# In[13]:


z = " " != ""  # Equivalente a z = (" " != "")
z


# In[14]:


x or z


# ### Reglas de precedencia

# - El orden de precedencia, de mayor a menor, es `not, and, or`. 
# - Estos operadores tienen menor prioridad que los operadores de comparación. 
# - Una buena práctica es usar paréntesis para evitar confusiones.

# In[15]:


x, y, z = False, True, True
x and not y or z  # Equivalente a (x and (not y)) or z


# ### Algebra Booleana

# - Doble Negación:
#     - `not (not x) == x`
# 
# - Ley Comutativa:
#     - `x and y == y and x`
#     - `x or y == y or x`
# 
# - Ley Asociativa:
#     - `(x and y) and z == x and (y and z)`
#     - `(x or y) or z == x or (y or z)`
# 
# - Ley Distributiva:
#     - `x and (y or z) == (x and y) or (x and z)`
#     - `x or (y and z) == (x or y) and (x or z)`
# 
# - Leyed de DeMorgan:
#     - `not (x and y) == (not x) or (not y)`
#     - `not (x or y) == (not x) and (not y)`

# - En un juego de dados, un jugador gana si tira dos seises con dos dados: `(d1 == 6) and (d2 == 6)`;
# - Pierde con otras combinaciones de números: `not ((d1 == 6) and (d2 == 6))`.
# - Podemos reescribir la condición perdedora como `(not (d1 == 6)) or (not (d2 == 6))`, que es equivalente a`(d1 != 6) or (d2 != 6)`.

# ### Conversión de otros tipos de datos a booleanos

# - La función Python `bool` puede convertir otros tipos de datos integrados a un booleano.
# - Para un número (int o float), el valor `0` será convertido a uno `False`, Y un valor distinto de cero se convertirá en un `True`.
# - Para una secuencia (cadena, lista, tupla, dict, set), se convertirá en un `False` si está vacía y un `True` Si no está vacía.

# In[16]:


bool(0)


# In[17]:


bool(1)


# In[18]:


bool(-2.1)


# In[19]:


bool('hello')


# In[20]:


bool('')


# In[21]:


bool(['Apple', 10, -3.14])


# In[22]:


bool(())


# In[23]:


bool({3, 4, 5})


# ### Operación de cortocircuito

# - Python `and, or, not` Son operadores de cortocircuito.
# - Um `True` o `False` se devuelve tan pronto como se pueda determinar el resultado.
# 
# | Operacion | Resultado devuelto                                  |
# |:----------|:-------------------------------------------------|
# | x and y   | if x is False, then False (and ignore y); else y |
# | x or y    | if x is True, then True (and ignore y); else y   |
# | not x     | if x is False, then True; else False             |

# In[24]:


x, y = 3, -1
x >= 5 or y  # Equivalente a (x >= 5) o y


# - En otro juego de dados, el jugador gana si tira un 5 o 6 con un solo dado. 
# - ¿Podemos escribir la condición ganadora como `d1 == 5 or 6`? 
# - No, porque es equivalente a `(d1 == 5) or 6`, que es igual a 6, un número distinto de cero. Por lo tanto, cuando se usa como condición, siempre devuelve un `True`. 
# - La condición ganadora correcta es `d1 == 5 or d1 == 6`, que es equivalente a `(d1 == 5) or (d1 == 6)`

# - ¿Qué tipo de café te gustaría tomar, capuchino, café con leche o moca?

# In[25]:


def main():
    answer = input('¿Qué tipo de café te gustaría [café con leche]? ')  # café con leche es el default
    print('Ordenaste un', answer or 'café con leche')
    
main()


# In[26]:


main()


# In[ ]:




