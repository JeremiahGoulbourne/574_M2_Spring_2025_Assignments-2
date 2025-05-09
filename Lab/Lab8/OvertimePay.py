hourlyWage = eval(input("Enter hourly wage: "))
totalHoursWorked = eval(input("Enter total hours worked: "))

regularPay = 40 * hourlyWage
overtimePay = 1.5 * hourlyWage * (totalHoursWorked - 40)
grossPay = regularPay + overtimePay

print(f"Gross Pay: {grossPay}")\

print("Gross pay for the week: ", "$" + str(grossPay))

if overtimePay > 0:
    print(f"You received {str(overtimePay)} in overtime pay.")
else:
    print("You did not earn any overtime pay period.")