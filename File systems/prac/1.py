#  finding the word twinkle:

with open('poem.txt', 'r') as f:
    a= f.read()
    print(a)
    b= a.find("twinkle")
    c= a.count("twinkle")
    print("\nThe first apearance of the word Twinkle is at "+ str(b)+" position")
    print(f"And it is written {c} times")