
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

list_of_celsius_fahrenheit = [list_of_celsius, list_of_fahrenheits]

print("Celsius to Fahrenheit")
print("Conversion Table")
print("-----------------")  
print("Celsius\t\tFahrenheit")
print(*list_of_celsius_fahrenheit, sep="\n")

# for i in range(len(list_of_celsius)):
#     print(list_of_celsius[i] + '\t ' + list_of_fahrenheits[i])

# Sorta close
# for temps in zip(*list_of_celsius_fahrenheit):
#     print(*temps)


# print(*list_of_celsius, sep = "\n")
# print(*list_of_fahrenheits, sep = "\n")

