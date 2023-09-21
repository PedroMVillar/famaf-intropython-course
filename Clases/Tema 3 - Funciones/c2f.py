def input_temp():
    temp = float(input('Ingrese la temperatura en °C: '))
    return temp

def convert_temp(c = -500):
    f = 9/5 * c + 32
    return f
    
def output_temp(f):
    print('La temperature es', f, '°F.')
    
def main():
    c = input_temp()
    f = convert_temp(c)
    output_temp(f)

if __name__ == '__main__':
    main()
    