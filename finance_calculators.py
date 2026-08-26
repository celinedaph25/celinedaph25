import math

print ('''Hello! Welcome to the calculator!\n
        Investment: to calculate the amount of interest you'll earn on your investment
        Bond: to calculate the amount you'll have to pay on a home loan\n''')

choice= str(input("Enter either 'investment' or 'bond' from the menu above to proceed: "))

#Investment decision
if choice.lower() == "investment":
    print ("You chose " + choice)
    deposit = int(input("\nHow much is the deposit? "))
    perc = int(input("How much is the % interest? "))
    p = float(perc / 100)
    years = int(input("How many years is the investment? "))
    interest = input("Do you want simple or compound interest? ")
 
    if interest.lower() == "simple":
        total = float(deposit * (1 + (p * years)))
        print ("$" + str(round(total)))
    elif interest.lower() == "compound":
        total = float(deposit * math.pow((1 + p), years))
        print ("$" + str(round(total)))
    else:
        print ("Unable to verify decision. Please try again.")

##Bond decision

elif choice.lower() == "bond":
    print ("You chose " + choice)
    house = int(input("\nWhat is the value of the house? "))
    perc = int(input("How much is the % interest? "))
    p = float((perc / 100)/12)
    months = int(input("How many months are you planning to pay? "))
    repayment = float((p * house) / ((1 - (1+p) **(-months))))
    print ("$" + str(round(repayment)))
else: 
    print ("Unable to identify choice. Please try again.")




