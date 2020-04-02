
# Variables 
Celsius = 0



# Function to convert Celsius to Fahrenheit
def convToFahrenheit(Celsius):
    listOfFahrenheits = []
    while (Celsius != 110):
        fahrenheit = (Celsius * 9/5) + 32
        Celsius += 10
        listOfFahrenheits.append(fahrenheit)
    return (listOfFahrenheits)


print("Celsius to Fahrenheit")
print("Conversion Table")
print("-----------------")

list_of_fahrenheits = convToFahrenheit(Celsius)
print(*list_of_fahrenheits, sep = "\n") 