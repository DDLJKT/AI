cardnumber=input("Enter no. of card: ")
cardcolor=input("Enter color of card: ")
pofA=4/52
pofB=26/52
print("p(A)=>Probability of drawing card with no ", cardnumber, "=", round(pofA,2))
print("p(B)=>Probability of drawing card with color ", cardcolor, "=", round(pofB,2))
print("Joint probability of A and B = P(A) * P(B)")
pAandB=round(pofA * pofB, 2)
print("P(A and B) = ", pAandB)
print("There are ", pAandB * 100 , "% chances that of getting ", cardcolor, "card with number ", cardnumber)
