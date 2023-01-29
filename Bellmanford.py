n = int(input("Enter the Number of Nodes :"))
nodes = [99]*n
nodes[0] = 0
a = [[0]*n for i in range(n)]
e = int(input("Enter the Number of Edges :"))
for i in range(e):
    p, q, w = input("Enter the Connection and Weight :").split()
    a[int(p)][int(q)] = int(w)

for k in range(n-1):
    for i in range(n):
        for j in range(n):
            if a[i][j] != 0:
                if nodes[i]+a[i][j] < nodes[j]:
                    nodes[j] = nodes[i]+a[i][j]

print("99 - infinity ")
print("Shortest Path is :")
for i in range(n):
    print("0 -", i, "=", nodes[i])