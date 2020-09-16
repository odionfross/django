def temp_conversion(temperature, temp_unit):
    # new_temperature = 0
    if temp_unit == 'celcius' or temp_unit == 'Celcius':
        new_temperature = (5/9) * (temperature - 32)
        print("The new temperature is ", new_temperature, "Celcius")
    if temp_unit == 'fahrenheit' or temp_unit == 'Fahrenheit':
        new_temperature = (9/5) * (temperature - 32)
        print("The new temperature is ", new_temperature, "Fahrenheit")
    return new_temperature

print(temp_conversion(0, 'celcius'))
print(temp_conversion(32, 'Fahrenheit'))