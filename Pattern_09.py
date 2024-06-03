for i in range(5):
    #space
    for j in range(5-i-1):
        print(end=" ")
    #star
    for k in range(i*2+1):
        print("*", end="")
    #space
    for l in range(5-i-1):
        print(end=" ")
    print()

for i in range(5):
    #space
    for j in range(i):
        print(end=" ")
    #star
    for k in range(10 - (2*i + 1)):
        print("*", end="")
    #space
    for l in range(i):
        print(end=" ")
    print()


#     *    
#    ***   
#   *****  
#  ******* 
# *********
# *********
#  ******* 
#   *****  
#    ***   
#     *