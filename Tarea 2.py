# -- coding: utf-8 --
"""
Spyder Editor

This is a temporary script file.
"""
import numpy

def printGraph(graph):
    k=0
    for k in range(0,len(graph)):
        print graph[k]
t,b,f,c = raw_input("Enter t b f c: ").strip().split(' ') #Input the tree, backward, forward and cross edges
t,b,f,c = [int(t),int(b),int(f),int(c)] #Convert the strings to ints.
#t,b,f,c = [3,1,1,1]
n = t+1 #Number of Nodes.
graph = numpy.zeros(shape=(n,n)) #Rows are existing Nodes. Columns are its connections with other nodes.
#Create tree edges
graph[0][1] = 1
if(t>1): 
    graph[0][2] = 1
    for i in range(2,t):
        graph[i][i+1] = 1

#Create backward edges
j = t
i = 1
while b>0:
    if (j-i != 1):
        graph[j][j-i] = 1
        i += 1
        b -= 1
    elif (j-i == 1):
        graph[j][0] = 1
        i += 1
        b -= 1
    else:
        i += 1
    if (i==j):
        i = 1
        j -= 1
        
#Create forward edges
u = n - 1
d = 0
while f>0:
    if (u!= (2 or d+1)):
        graph[d][u] = 1
        u -= 1
        f -= 1
    else:
        if(d==0):
            d += 2
        else:
            d += 1
        u = n - 1

#Create cross edges
j = n-1
while c>0:
    if j == 1:
        j -= 1
        continue
    graph[1][j] = 1
    j -= 1
    c -= 1
print "Adjacency Matrix: "
printGraph(graph) #Final Graph's Matrix

#Real Output
print " "
k = 0
h = 0
edge = 0
for  k in range(0, n):
    l =" "
    for h in range(0, n):
       if graph[k][h] == 1 :
           l += str(h+1) + " "
           edge +=1
    l = str(edge) + l
    print l
    edge = 0
        
        

        
        