def convert_cel_to_far(C):
    return round(C*(9/5) +32,2)

def convert_far_to_cel(F):
    return round((F-32)*(5/9),2)

fahrenheitInput = input('Enter a temperature in degrees Fahrenheit: ')
celsiusInput = input('Enter a temperature in degrees Celsius: ')

print(f"F->C {convert_far_to_cel(float(fahrenheitInput))}")
print(f"C->F {convert_cel_to_far(float(celsiusInput))}")