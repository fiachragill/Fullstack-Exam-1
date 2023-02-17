# 11111111111111111
#  222222222222222
#   3333333333333
#    44444444444
#     555555555
#      6666666
#       77777
#        888
#         9

n = 9
nums = [n for n in range(1, n+1)]
i = 1
edge = 2 

for n in nums[::-1]:
    if i == 1:
        print(n)
    elif i == 2:
        print((str(n))*(edge))
    else:
        print((str(n))*(edge+1))

    edge += 1
    i += 1
    
