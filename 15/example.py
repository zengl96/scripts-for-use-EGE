
# отрезки


# for x in [k*0.25 for k in range(-10_100,10_1000)]:

#     p = 12 <= x <= 26
#     q = 30 <= x <= 53
#     A = 1 # наименьшее это 0 наибольшее это 1

#     f = ( ( (A) <= (p)   ) or q   )

#     if  f != 0: # истина то != not A ложно то != A
#         print(x)



# все остальные типы перебором

def r(x,y,A):

    return (x+2*y < A) or (y>x) or (x>60)

n = 100000
_ = True
for A in range(0,200):

    for x in range(200):
        for y in range(200):

            if r(x,y,A) == 0:
                _ = False
    
    if _ == True:
        n = min(n, A)
        print(n)
    
    _ = True





# множества решается так же как отрезки