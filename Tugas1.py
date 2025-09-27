image = [[-3,-2,-1,-4,-5],
            [-4,-3,2,0,1],
            [-3,3,0,2,1],
            [1,0,2,-3,4],
            [0,1,-4,-1,2],         
         ]

for i in range(len(image)):
    for j in range(len(image[0])):
        image[i][j] = max(0,image[i][j])

for i in range(len(image)):
    for j in range(len(image[0])):
        print(image[i][j],end=" ")

flatten = []

for i in range(len(image)):
    for j in range(len(image[0])):
        flatten.append(image[i][j])

print("\nHasil Flatten: ")
print(flatten)
