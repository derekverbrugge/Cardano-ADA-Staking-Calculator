# Constants (adjust these values as needed)
total_ada_staked = 10_000_000  # Total ADA staked in your pool
annual_reward_rate = 0.05  # Annual reward rate (5% as an example)

# User inputs
staked_amount = float(input("Enter the amount of ADA you want to stake: "))
# Measure in: 1 Epochs 2 Days 3 Months 4 Years
evdvmvy = 4

#int(input("Caluclate for: 1. epochs 2. days 3. months 4. years? Enter a number to choose: "))

# Duration: An epoch is 5 days. 6 epochs is roughly 1 month, and 73 epochs is 1 year. 
if evdvmvy == 1:
  staking_duration = int(input("Enter the number of epochs you plan to stake for: "))
  period = "epochs"
if evdvmvy == 2:
  staking_duration = (((73 / 365) * (int(input("Enter the number of days you plan to stake for: "))))
  period = "days"
if evdvmvy == 3:
  staking_duration = ((73 / 12) * (int(input("Enter the number of months you plan to stake for: "))))
  period = "months"
if evdvmvy == 4:
  staking_duration = (73 * (int(input("Enter the number of years you plan to stake for: "))))
  period = "years"

# Calculate rewards
epoch_length = 5 * 24 * 3600  # Length of an epoch in seconds (5 days). 
reward_per_epoch = (staked_amount / total_ada_staked) * (annual_reward_rate / 365) * epoch_length
total_rewards = reward_per_epoch * staking_duration

# Display results
print(f"Estimated staking rewards after {staking_duration} {period}:")
print(f"Staked ADA: {staked_amount} ADA")
print(f"Total rewards: {total_rewards:.2f} ADA")
