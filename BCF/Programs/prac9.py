import random

class Validator:
    def __init__(self, name, stake):
        self.name = name
        self.stake = stake

    def __str__(self):
        return f"{self.name} (Stake: {self.stake})"

validators = [
    Validator("Alice", 50),
    Validator("Bob", 30),
    Validator("Charlie", 15),
    Validator("Diana", 5),
]

def build_staking_pool(validators):
    pool = []
    for v in validators:
        pool.extend([v] * v.stake)
    return pool

def select_validator(pool):
    return random.choice(pool)

def simulate_pos_rounds(validators, rounds=10):
    pool = build_staking_pool(validators)
    print("Validators in the network:")
    for v in validators:
        print(f" - {v}")

    print("\n--- Block Validation Rounds ---")
    for i in range(rounds):
        winner = select_validator(pool)
        print(f"Round {i+1}: Block validated by {winner.name}")

simulate_pos_rounds(validators, rounds=10)