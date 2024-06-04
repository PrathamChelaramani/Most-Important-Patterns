space1 = 8
for i in range(5):
    #star
    for j in range(i+1):
        print("*", end=" ")

    #spaces
    for k in range(space1):
        print(end="  ")

    #star
    for j in range(i+1):
        print("*", end=" ")
    print()
    space1-=2

space2 = 2
for i in range(4):
    #star
    for j in range(4-i):
        print("*", end=" ")

    #spaces
    for k in range(space2):
        print(end="  ")

    #star
    for j in range(4-i):
        print("*", end=" ")
    print()
    space2+=2



# *                 * 
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *