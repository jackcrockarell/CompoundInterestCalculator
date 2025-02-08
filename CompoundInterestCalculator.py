#Compound interest is when you add the earned interest back into your principal
#This program will calculate the amount of money accrued after some time.
#The user will decide the initial principle, interest rate, and time that has passed

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate amount: "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break

total = principle * pow(1 + rate / 100, time)
print(f"Balance after {time} year/s: $ {total:.2f}")
