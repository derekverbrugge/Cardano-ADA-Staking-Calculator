principle = 2300
years = 10
rate = 0.05
epochs = 73 #this is the compounding frequency ADA epochs are roughly 5 days
min = .9262
max = 1.1926

reward = principle * (1 + (rate / epochs))**(epochs * years)
fiveyreward = principle * (1 + (rate / epochs))**(epochs * 5)
year_reward = (principle * rate)

print(f"Day: {(year_reward / 365) * min:.2f} ADA - {(year_reward / 365) * max:.2f} ADA (average of {year_reward / 365:.2f} ADA)")
print(f"Epoch: {(year_reward / epochs) * min:.2f} ADA - {(year_reward / epochs) * max:.2f} ADA (average of {year_reward / epochs:.2f} ADA)")
print(f"Month: {(year_reward / 12) * min:.2f} ADA - {(year_reward / 12) * max:.2f} ADA (average of {year_reward / 12:.2f} ADA)")
print(f"Year: {year_reward * min:.2f} ADA - {year_reward * max:.2f} ADA (average of {year_reward:.2f} ADA) ") 
print(f"Total accumulated after 1 year: {principle + year_reward * min:.2f} ADA - {principle + year_reward * max:.2f} (average of {(principle + year_reward):.2f} ADA (including priciple))")
if years >= 5:
    print(f"Total accumulated after 5 years: {fiveyreward * min:.2f} ADA - {fiveyreward * max:.2f} ADA (average of {fiveyreward:.2f} ADA (including priciple))")
if 1 < years != 5:
    print(f"Total accumulated after {years} years: {reward * min:.2f} ADA - {reward * max:.2f} ADA (average of {reward:.2f} ADA (including priciple))")

    
    
