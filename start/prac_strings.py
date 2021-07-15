# Q1
a=input("Enter Name ")
print("Good Afternoon,", a)


# Q2
letter= '''Dear <|NAME|>,

    You are selected!

    <|DATE|>
'''
name=input("Enter your name:\n")
date=input("Enter Date:\n")
letter=letter.replace("<|NAME|>", name)

letter=letter.replace("<|DATE|>", date)

print(letter)

# Q3
p=''' Hi i am avik khanna  
i want to become an  ethical hacker;
please could you help me to achieve my wonderful goal!!   '''
doublespace=p.find("  ")
print(doublespace)


# Q4
p=''' Hi i am avik khanna  
i want to become an  ethical hacker;
please could you help me to achieve my wonderful goal!!   '''
p=p.replace("  ", " ")
print(p)

# Q5
letter="Dear Harry,\n\tThis Python Course is nice!\nThanks!"
print(letter)