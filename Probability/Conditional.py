pofA = float(input ("Enter no. of C programmers in percentage "))
pofAandB = float(input("Enter no. of C and Java programmers in percentage "))
pofA = pofA/100
pofAandB = pofAandB/100
print("Event B that student is Java programmer=?")
print("Event A that student is C programmer=",pofA)
print("Event A and B that is student knowing both C and java is= ",pofAandB)
print("Lets calculate P(B/A)=P(AandB)/P(A)")
pBgivenA=pofAandB/pofA
print("P(B/A)=",pBgivenA)
print("There are",pBgivenA*100,"% chances that the student that knows A also knows Java")
