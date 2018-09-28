a = 3
b = 4
c = a + b
PI = 3.14159
e = .342523 # to be printed as a percent
bank_balance = 239432.82
# Print this EXACT thing (with same exact spaces):
# a = 3, b = 4, c = 7

print("a = {}, b = {}, c = {}".format(a,b,c))

print("PI = {:.2f}".format(PI))
print("The percentage value of \"e\" is {:.2%}.".format(e)) #turns it into a percentage
print("You're bank balance is ${:,.2f}.".format(bank_balance)) #adds commas