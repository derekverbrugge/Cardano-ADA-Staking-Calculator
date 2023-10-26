principle = float(input("Enter the amount of ADA you want to stake: "))
years = int(input("How many years should be calculated: "))
adaprice = float(input("Enter your target price of ADA in USD to estimate in USD or enter 1 or 0 to calculate in ADA: "))
rate = 0.05
epochs = 73 #this is the compounding frequency ADA epochs are roughly 5 days
min = .9262
max = 1.1926

reward = principle * (1 + (rate / epochs))**(epochs * years)
fiveyreward = principle * (1 + (rate / epochs))**(epochs * 5)
year_reward = (principle * rate)

if adaprice == 0 or adaprice == 1: 
    adaorusd = "ADA"
    dollarsym = ""
    usdmult = 1
else:
    adaorusd = "USD"
    dollarsym = "$"
    usdmult = adaprice
    

print(f"Day: {dollarsym}{((year_reward / 365) * min) * usdmult:.2f} {adaorusd} - {dollarsym}{((year_reward / 365) * max) * usdmult:.2f} {adaorusd} (average of {dollarsym}{(year_reward / 365) * usdmult:.2f} {adaorusd})")
print(f"Epoch: {dollarsym}{((year_reward / epochs) * min) * usdmult:.2f} {adaorusd} - {dollarsym}{((year_reward / epochs) * max) * usdmult:.2f} {adaorusd} (average of {dollarsym}{(year_reward / epochs) * usdmult:.2f} {adaorusd})")
print(f"Month: {dollarsym}{((year_reward / 12) * min) * usdmult:.2f} {adaorusd} - {dollarsym}{((year_reward / 12) * max) * usdmult:.2f} {adaorusd} (average of {dollarsym}{(year_reward / 12) * usdmult:.2f} {adaorusd})")
print(f"Year: {dollarsym}{(year_reward * min) * usdmult:.2f} {adaorusd} - {dollarsym}{(year_reward * max) * usdmult:.2f} {adaorusd} (average of {dollarsym}{(year_reward) * usdmult:.2f} {adaorusd}) ") 
print(f"Total accumulated after 1 year: {dollarsym}{(principle + year_reward * min) * usdmult:.2f} {adaorusd} - {dollarsym}{(principle + year_reward * max) * usdmult:.2f} {adaorusd} (average of {dollarsym}{(principle + year_reward) * usdmult:.2f} {adaorusd} (including priciple))")
if years >= 5:
    print(f"Total accumulated after 5 years: {dollarsym}{(fiveyreward * min) * usdmult:.2f} {adaorusd} - {dollarsym}{(fiveyreward * max) * usdmult:.2f} {adaorusd} (average of {dollarsym}{(fiveyreward) * usdmult:.2f} {adaorusd} (including priciple))")
if 1 < years != 5:
    print(f"Total accumulated after {years} years: {dollarsym}{(reward * min) * usdmult:.2f} {adaorusd} - {dollarsym}{(reward * max) * usdmult:.2f} {adaorusd} (average of {dollarsym}{(reward) * usdmult:.2f} {adaorusd} (including priciple))")

    
    
