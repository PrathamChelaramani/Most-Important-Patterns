inis = 0
for i in range(5):
    #star
    for j in range(5-i):
        print("*", end=" ")

    #space
    for k in range(inis):
        print(end="  ")

    #star
    for l in range(5-i):
        print("*", end=" ")
    print()
    inis+=2

n=5
iniS = 8
for i in range(n):
    #star
    for j in range(i+1):
        print("*", end=" ")
    
    #space
    for k in range(iniS):
        print(end="  ")

    #star
    for l in range(i+1):
        print("*", end=" ")
    print()
    iniS-=2




# * * * * * * * * * * 
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *