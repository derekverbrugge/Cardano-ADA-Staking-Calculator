# Constants (adjust these values as needed)
#total_ada_staked = 10_000_000  # Total ADA staked in your pool
annual_reward_rate = 0.05  # Annual reward rate (5% as an example)

# User inputs
staked_amount = float(input("Enter the amount of ADA you want to stake: "))
# staking_duration = int(input("Enter the number of epochs you plan to stake for: "))
# Measure in: 1 Epochs 2 Days 3 Months 4 Years
evdvmvy = int(input("Caluclate for: 1. epochs 2. days 3. months 4. years? Enter a number to choose: "))

# Duration: An epoch is 5 days. 6 epochs is roughly 1 month, and 73 epochs is 1 year. 
if evdvmvy == 1:
    period = "epochs"
    staking_duration = int(input("Enter the number of " + period + " you plan to stake for: "))
  
if evdvmvy == 2:
    period = "days"
    staking_duration = int(input("Enter the number of " + period + " you plan to stake for: "))
  
if evdvmvy == 3:
    period = "months"
    staking_duration = int(input("Enter the number of " + period + " you plan to stake for: "))
if evdvmvy == 4:
    period = "years"
    staking_duration = int(input("Enter the number of " + period + " you plan to stake for: "))
  
# Calculate rewards
epoch_length = 5 * 24 * 3600  # Length of an epoch in seconds (5 days)
reward_per_year = staked_amount * annual_reward_rate
if evdvmvy == 1:
    total_rewards = (reward_per_year * staking_duration) / 365
if evdvmvy == 2:
    total_rewards = ((reward_per_year * staking_duration) / 365) * 5
if evdvmvy == 3:
    total_rewards = (reward_per_year * staking_duration) / 12
if evdvmvy == 4:
    total_rewards = reward_per_year * staking_duration    

#calculate high and low estimate
total_rewardsL = total_rewards * .9262
total_rewardsH = total_rewards * 1.1926

# Display results
print(f"Estimated staking rewards after {staking_duration} {period}:")
print(f"Staked ADA: {staked_amount} ADA")

print(f"Total rewards (Low Estimate): {total_rewardsL:.2f} ADA")
print(f"Total rewards (High Estimate): {total_rewardsH:.2f} ADA")
