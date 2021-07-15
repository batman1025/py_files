# translation of hindi to eng dictionary

mydict={
    "saanp":"snake",
    "pankha": "fan",
    "pankh": "wings",
    "tez"   : "fast"
    }
print("options are\n", mydict.keys())
n=input("Enter word to be searched : ")
print("the meaning of your entered word is: ", mydict.get(n)) 