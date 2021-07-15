with open('log.txt') as f:
    content= f.read().lower()
                                #  if the letter to be found is captital so we can add .lower at end
if 'python' in content:
    print("yes python is present")
else:
    print("no python is not present")
    