
# clastersA = [[], []]

clastersB = [[], [], []]


# for line in open('27/27A_18630.txt'):
#     x, y = [float(k) for k in line.split()]

#     if (x-1)**2+(y-6)**2<=25:
#         clastersA[0].append([x,y])
#     elif (x-9)**2+(y-5)**2<=16:
#         clastersA[1].append([x,y])



for line in open('27/27B_18630.txt'):
    x, y = [float(k) for k in line.split()]

    if (y>(-2/6)*x+(34/3)) and (y>x-5):
        clastersB[0].append([x,y])
    elif (y<(-2/6)*x+(34/3)) and x > 10:
        clastersB[1].append([x,y])
    elif (y<-0.2*x+8.4) and x < 10:
        clastersB[2].append([x,y])






def lenght(a,b):

    l = ((b[0]-a[0])**2+((b[1]-a[1])**2))**0.5

    return l


def main(cl):
    m = []
    for a in cl:
        g = sum(lenght(a,b) for b in cl)
        m.append([g,a])

    return min(m)



# print((main(clastersA[0])[1][0]+main(clastersA[-1])[1][0])/2*100_000)
# print((main(clastersA[0])[1][1]+main(clastersA[-1])[1][1])/2*100_000)

print((main(clastersB[0])[1][0]+main(clastersB[1])[1][0]+main(clastersB[2])[1][0])/3*100_000)
print((main(clastersB[0])[1][1]+main(clastersB[1])[1][1]+main(clastersB[2])[1][1])/3*100_000)


