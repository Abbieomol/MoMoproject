import json
import time
import random

# Load the JSON data
with open("parsed_sms_v2.json", "r") as f:
    transactions = json.load(f)

# Make sure IDs are integers (easier for lookups)
for t in transactions:
    t["id"] = int(t["id"])

# --- Linear search through the list ---
def linear_lookup(transactions, target_id):
    for t in transactions:
        if t["id"] == target_id:
            return t
    return None

# --- Dictionary lookup ---
# Build a dictionary keyed by transaction id
transaction_dict = {t["id"]: t for t in transactions}

def dict_lookup(tx_dict, target_id):
    return tx_dict.get(target_id)

# --- Benchmark setup ---
num_trials = 10000
all_ids = [t["id"] for t in transactions]

# Time linear search
start = time.time()
for _ in range(num_trials):
    test_id = random.choice(all_ids)
    linear_lookup(transactions, test_id)
linear_duration = time.time() - start

# Time dictionary lookup
start = time.time()
for _ in range(num_trials):
    test_id = random.choice(all_ids)
    dict_lookup(transaction_dict, test_id)
dict_duration = time.time() - start

# Print results
print(f"Linear search ({num_trials} lookups): {linear_duration:.6f} sec")
print(f"Dictionary lookup ({num_trials} lookups): {dict_duration:.6f} sec")
print(f"Dictionary method was about {linear_duration / dict_duration:.2f}x faster")
