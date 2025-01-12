

cA = [[], [], []]


for line in open('27/27B_18678.txt'):

    x,y = [float(i) for i in line.split('\t')]

    if y> 1.5 and y<7 and x>3 and x<6.1:
        cA[0].append([x,y])
    elif y< (-11/4)*x+(51/4) and x<4.5:
        cA[1].append([x,y])
    elif (y>-1*x+13 or y<6*x-36) and y<-1*x+18:
        cA[2].append([x,y])


def find_distance(a,b):


    return ( (b[0]-a[0])**2+(b[1]-a[1])**2    )**0.5


def main(cl):

    list_sum = []
    for a in cl:

        t = sum(find_distance(a,b) for b in cl)
        list_sum.append([t, a])

    return min(list_sum)


# print((main(cA[0])[1][0]+main(cA[-1])[1][0])/2*100_000)
# print((main(cA[0])[1][1]+main(cA[-1])[1][1])/2*100_000)

print((main(cA[0])[1][0]+main(cA[1])[1][0]+main(cA[-1])[1][0])/3*100_000)
print((main(cA[0])[1][1]+main(cA[1])[1][1]+main(cA[-1])[1][1])/3*100_000)


# print(  (main(cA[0])[1][0]+main(cA[1])[1][0])/2*100_000     )
# print(  (main(cA[0])[1][1]+main(cA[1])[1][1])/2*100_000     )