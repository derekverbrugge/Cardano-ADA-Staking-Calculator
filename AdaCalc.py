
# Inspired by the adatainment ada staking calculator @ https://www.adatainment.com/index.php?page=staking_calculator 
# Based on IOHK's literature @ https://iohk.io/en/research/library/#reward-sharing-schemes-for-stake-pools

principle = float(input("Enter the amount of ADA you want to stake: ")) #initial investment amount in ADA
years = int(input("How many years should be calculated: ")) #number of years staking rewards will be calculated to.
adaprice = float(input("Enter your target price of ADA in USD to estimate in USD or enter 1 or 0 to calculate in ADA: "))
rate = 0.05 #staking rewards
epochs = 73 #this is the compounding frequency. ADA epochs are roughly 5 days.

#min and max represent variance depending on the staking pool.

min = .9262 
max = 1.1926

reward = principle * (1 + (rate / epochs))**(epochs * years) #reward calculated with compounding interest.
fiveyreward = principle * (1 + (rate / epochs))**(epochs * 5) #five year reward calculated with compounding interest.
year_reward = (principle * rate) #reward for a year.

#change symbols and denomination and apply multiplier for USD as necessary.
if adaprice == 0 or adaprice == 1: 
    adaorusd = "ADA"
    dollarsym = ""
    usdmult = 1
    if adaprice == 1:
        adaorusd = "ADA/USD"
else:
    adaorusd = "USD"
    dollarsym = "$"
    usdmult = adaprice

    
#print results
print("")
if adaprice == 0 or adaprice == 1:
    print(f"Rewards on {principle:.2f} {adaorusd} for the 1st year.")
else:
    print(f"Rewards on {principle:.2f} ADA or {dollarsym}{(adaprice * principle):.2f} USD @ {dollarsym}{adaprice:.2f} USD/ADA for the 1st year.")
print(f"Day:    {dollarsym}{(year_reward / 365) * usdmult:.2f} {adaorusd} ({dollarsym}{((year_reward / 365) * min) * usdmult:.2f} {adaorusd} - {dollarsym}{((year_reward / 365) * max) * usdmult:.2f} {adaorusd})")
print(f"Epoch:  {dollarsym}{(year_reward / epochs) * usdmult:.2f} {adaorusd} ({dollarsym}{((year_reward / epochs) * min) * usdmult:.2f} {adaorusd} - {dollarsym}{((year_reward / epochs) * max) * usdmult:.2f} {adaorusd})")
print(f"Month:  {dollarsym}{(year_reward / 12) * usdmult:.2f} {adaorusd} ({dollarsym}{((year_reward / 12) * min) * usdmult:.2f} {adaorusd} - {dollarsym}{((year_reward / 12) * max) * usdmult:.2f} {adaorusd})")
print(f"Year:   {dollarsym}{(year_reward) * usdmult:.2f} {adaorusd} ({dollarsym}{(year_reward * min) * usdmult:.2f} {adaorusd} - {dollarsym}{(year_reward * max) * usdmult:.2f} {adaorusd}) ") 
if years >= 1:
    if years > 9: 
        space = ' '
        if years > 99: 
            space = '  '
    else: space = ''
    print("")
    
    print(f"Total accumulated up to {years} years.")
    print(f"{space}1 year:  {dollarsym}{(principle + year_reward) * usdmult:.2f} {adaorusd} | ({dollarsym}{(principle + year_reward * min) * usdmult:.2f} {adaorusd} - {dollarsym}{(principle + year_reward * max) * usdmult:.2f} {adaorusd})")
if years >= 5:
    print(f"{space}5 years: {dollarsym}{(fiveyreward) * usdmult:.2f} {adaorusd} | ({dollarsym}{(fiveyreward * min) * usdmult:.2f} {adaorusd} - {dollarsym}{(fiveyreward * max) * usdmult:.2f} {adaorusd})")
if 1 < years != 5:
    print(f"{years} years: {dollarsym}{(reward) * usdmult:.2f} {adaorusd} | ({dollarsym}{(reward * min) * usdmult:.2f} {adaorusd} - {dollarsym}{(reward * max) * usdmult:.2f} {adaorusd})")

    
    
