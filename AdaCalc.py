# Constants (adjust these values as needed)
total_ada_staked = 10_000_000  # Total ADA staked in your pool
annual_reward_rate = 0.05  # Annual reward rate (5% as an example)

# User inputs
staked_amount = float(input("Enter the amount of ADA you want to stake: "))
staking_duration = int(input("Enter the number of epochs you plan to stake for: "))

# Calculate rewards
epoch_length = 5 * 24 * 3600  # Length of an epoch in seconds (5 days)
reward_per_epoch = (staked_amount / total_ada_staked) * (annual_reward_rate / 365) * epoch_length
total_rewards = reward_per_epoch * staking_duration

# Display results
print(f"Estimated staking rewards after {staking_duration} epochs:")
print(f"Staked ADA: {staked_amount} ADA")
print(f"Total rewards: {total_rewards:.2f} ADA")
