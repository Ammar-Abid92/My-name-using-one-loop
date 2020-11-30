# a = 10
# for row in range(7):
#     if row == 3:
#         print(a*" ", 9 * "^")
#     print(a*" ", "^", 5*" ", "^")

a = 20
for b in range(25):
    if b % 2 != 0:
        print(a*"  ", b*" *")
        a = a-1
