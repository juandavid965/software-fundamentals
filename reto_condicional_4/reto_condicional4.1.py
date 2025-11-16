# declare variables or constants
# initiliazae variables or constants
num1 = 0
num2 = 0

# get number 1
num1 = float(input("enter value to number 1: "))

# get number 2
num2 = float(input("enter value to number 2: "))

#printo math meni 
print('''math menu: 
      [1]. add 
      [2]. subs   
      [3]. mult 
      [4]. div 
      [5]. all
''')

opt = int(input("press any option [1 - 5]"))
if opt == 1:
    res = num1 + num2
    print("addition: " + str(res))
else:
    if opt == 2:
        res = num1 - num2
        print("substraction" + str(res))
    else:
        if opt == 3:
            res = num1 * num2
            print("multiplicacion: " + str(res))
        else:
            if opt == 4:
                res = num1 / num2
                print("division: " + str(res))
            else:
                if opt == 5:
                    print("add: " + str(num1 + num2))
                    print("subs: " + str(num1 - num2))
                    print("mult: " + str(num1 * num2))
                    print("div: " + str(num1 / num2))
                else:
                    print("invalid option ")
