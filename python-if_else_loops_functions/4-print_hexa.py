#!/usr/bin/python3
for number in range(0,99):
    hexa_unit = number % 16
    hexa = number //16
    

    if hexa_unit >= 10 and hexa_unit <= 15:
        hexa_unit += 55 
        hexa_unit = chr(hexa_unit)

    if hexa >= 10 and hexa <= 15:
        hexa += 55 
        hexa = chr(hexa)
    
    if hexa != 0:
        print(f"{number} = 0x{hexa}{hexa_unit}")
    else:
        print(f"{number} = 0x{hexa_unit}")
        
