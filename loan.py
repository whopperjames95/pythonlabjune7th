#purpose: get loan details

money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("what is the APR?\n"))
payment = float(input("What will your monthly payment be in dollars? \n"))
months = int(input("How many months do you want to see results for? \n"))

monthly_rate = apr/100/12

for i in range(months):
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("you paid off the loan in", i+1, "months")

    money_owed = money_owed - payment

    print("paid", payment, "of which", interest_paid, "was interest", end= " ")
    print("Now i owe", money_owed)