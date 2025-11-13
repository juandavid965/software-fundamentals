from random import randint
def calc_add1(x, y):
    add= x + y
    print(f"[f1. without retunr] addition is: {add}") 

def calc_add1(x, y):
    add= x + y
    return add 

##################### Main #################
n1 = randint (1, 1000)
n2 = randint (1, 1000)

calc_add1(n1,n2)
answer = calc_add1(n1,n2)
print(print(f"addition is: {answer}"))