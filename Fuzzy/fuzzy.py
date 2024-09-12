elt=['w','x','y','z']
A=[0.5,0.4,0.3,0.2]
B=[0.2,0.1,0.2,1]
def printset(m):
    for i in range(0,4):
        print("(",elt[i],",",m[i],")",end=",")
    print()
print("Set A=")
print(A)
print("Set B=")
print(B)

#union
U=[]
for i in range(0,4):
    if A[i]>B[i]:
        U.append(A[i])
    else:
        U.append(B[i])
print("Union=")
printset(U)

#intersection
I=[]
for i in range(0,4):
    if A[i]<B[i]:
        I.append(A[i])
    else:
        I.append(B[i])
print("Intersection=")
printset(I)

#A complement
AC=[]
for i in range(0,4):
    AC.append(1-A[i])
print("A'=")
printset(AC)

#B Complement
BC=[]
for i in range(0,4):
    BC.append(1-B[i])
print("B'=")
printset(BC)

#difference A-B(min(A,BC))
AMB=[]
for i in range(0,4):
    if A[i]<BC[i]:
        AMB.append(A[i])
    else:
        AMB.append(BC[i])
print("Difference A-B=")
printset(AMB)

#difference of B-A(min(B,AC))
BMA=[]
for i in range(0,4):
    if B[i]<AC[i]:
        BMA.append(B[i])
    else:
        BMA.append(AC[i])
print("Difference B-A=")
printset(BMA)
