
# Variables 
Celsius = 0
list_of_celsius = [
    0,
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100
]

# Function to convert Celsius to Fahrenheit
def convToFahrenheit(Celsius):
    listOfFahrenheits = []
    while (Celsius != 110):
        fahrenheit = (Celsius * 9/5) + 32
        Celsius += 10
        listOfFahrenheits.append(fahrenheit)
    return (listOfFahrenheits)

list_of_fahrenheits = convToFahrenheit(Celsius)

print("Celsius to Fahrenheit")
print("Conversion Table")
print("-----------------")  
print("Celsius\t\tFahrenheit")


print(*list_of_celsius, sep = "\n")
print(*list_of_fahrenheits, sep = "\n")

