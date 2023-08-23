import math
def Googol(input_tid):
    googol_timmar = (10**100)/60
    googol_timmar_under_24 = googol_timmar % 24
    ny_tid = input_tid + googol_timmar_under_24 
    
    while ny_tid > 24:
        ny_tid = ny_tid - 24
    return ny_tid
print(Googol(13))

print(float("3.14"))

x = complex(1+1j)
print(2**(x))

print(x/3)
print(x%3)