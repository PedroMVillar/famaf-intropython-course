# Python 3: Fibonacci series up to n
def input_n():
    num = int(input('Ingrese el numero entero n: '))
    return num  


def fib(num):
    """Generador de n primeros numeros de Fibonacci"""
    i = 0
    a, b = 0, 1
    while i < num:
        i += 1
        yield a            # devolvemos un valor. En el proximo llamado retornará desde este punto, 
        print(i,a,b)                  # con los valores de locals() tal como estaban antes de hacer el yield
        a, b = b, a + b



num = input_n()

pirulo=list(fib(num))
print(pirulo)



