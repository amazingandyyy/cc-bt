import math

amount = float(input("How big is your debt? "))
transfer_fee = float(input("What % is the transfer fee? "))/100*amount
apr = float(input("What is the APR for the debt? "))/100
daily_rate = apr/365
days = 1
accumulate_interest = (amount*math.pow(1+daily_rate, days)-amount)
while transfer_fee > accumulate_interest:
 days = days + 1
 accumulate_interest = (amount*math.pow(1+daily_rate, days)-amount)

print("DAYS" + str(days))
print("If you cannot pay $" + str(amount) + " in " + str(days) + " days, it's worthy to do this balance transfer!")