import math

debt_size = float(input("How big is your debt? "))
apr = float(input("What is the APR for the debt? "))/100
transfer_fee = (float(input("What % is the transfer fee? "))/100)*debt_size
daily_rate = apr/365
days = 1
accumulate_interest = (debt_size*math.pow(1+daily_rate, days)-debt_size)
while transfer_fee > accumulate_interest:
 days = days + 1
 accumulate_interest = (debt_size*math.pow(1+daily_rate, days)-debt_size)

answer = input("Can you pay $"+ str(debt_size) + " in " + str(days) + "days?[y/n]")
if answer == "n":
 print("OKAY: It may be worthy to transfer $"+ str(debt_size) + "right now!")
elif answer == "y":
 print("Well, it is NOT worthy to transfer!")
