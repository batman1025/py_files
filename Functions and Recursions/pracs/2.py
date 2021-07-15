# Fahrenheit (°F) = (Celsius x 1.8) + 32 

def conv(a):
    f=(a*1.8)+32
    print(f"After converting we get {f}")
    
b=int(input("Enter temperature in celsius : "))
conv(b)