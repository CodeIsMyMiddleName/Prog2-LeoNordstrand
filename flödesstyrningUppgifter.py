import math
"""def hej():
    for i in range(1000):
        if i % 7 == 0:
            print(i)
"""

def antal_siffror(input_str):
    siffermängd = 0
    siffror = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    for element in input_str:
        if element in siffror:
            siffermängd += 1
    return siffermängd

def is_primtal(tal):
    for cool in range(2, math.ceil(tal / 2) + 1):
        if tal % cool == 0:
            return False
    return True
    

def tusende_primtalet():
    antal_primtal = 0
    nuvarande_tal = 0
    while antal_primtal < 1002:  

        if is_primtal(nuvarande_tal):
            antal_primtal += 1
        nuvarande_tal += 1 

    return nuvarande_tal - 1
    
def coola_primtal():
    antal_primtal = [1, 2]
    nuvarande_tal = 0
    while True:  

        if is_primtal(nuvarande_tal):
            antal_primtal.append(nuvarande_tal)
            if len(str(antal_primtal[-1] * antal_primtal[-2]))>= 10:
                return (antal_primtal[-1], antal_primtal[-2])
                
        nuvarande_tal += 1


print(coola_primtal())


