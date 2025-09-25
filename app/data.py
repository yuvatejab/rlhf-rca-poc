import random
from datasets import Dataset


events = ["API latency spike", "database connection failure", "user login outage", "payment processing error"]
services = ["authentication service", "caching layer", "primary database", "billing API"]
issues = ["a memory leak", "a misconfiguration in the firewall", "an expired SSL certificate", "a bug in the new deployment"]
actions = ["restarting the pods", "rolling back the deployment", "issuing a hotfix", "renewing the certificate"]

def generate_rca_pair():
    
   
    event = random.choice(events)
    service = random.choice(services)
    issue = random.choice(issues)
    action = random.choice(actions)
    
    prompt = f"Provide a Root Cause Analysis for the recent {event}."
    
    chosen = f"The root cause of the {event} was conclusively identified as {issue} in the {service}. The issue has been resolved by {action}."
    
    rejected = f"It is unclear what caused the {event}. There might be a possible issue with the {service}, but the investigation was inconclusive."
    
    return {"prompt": prompt, 
            "chosen": chosen, 
            "rejected": rejected}




# Assuming the generate_rca_pair() function from before is defined

# 1. Generate our synthetic data
output_list = []
for _ in range(500): # Create 500 examples
    output_list.append(generate_rca_pair())

# 2. Convert the list of dictionaries to a Hugging Face Dataset
dataset = Dataset.from_list(output_list)

# 3. Define a function to tokenize the chosen and rejected texts
def preprocess_function(examples):
    # The tokenizer will turn our text into numbers (input_ids)
    new_examples = {
        "input_ids_chosen": [],
        "attention_mask_chosen": [],
        "input_ids_rejected": [],
        "attention_mask_rejected": [],
    }
    for chosen, rejected in zip(examples["chosen"], examples["rejected"]):
        tokenized_chosen = tokenizer(chosen, truncation=True)
        tokenized_rejected = tokenizer(rejected, truncation=True)
        
        new_examples["input_ids_chosen"].append(tokenized_chosen["input_ids"])
        new_examples["attention_mask_chosen"].append(tokenized_chosen["attention_mask"])
        new_examples["input_ids_rejected"].append(tokenized_rejected["input_ids"])
        new_examples["attention_mask_rejected"].append(tokenized_rejected["attention_mask"])
        
    return new_examples

# 4. Apply the tokenization function to our dataset
# The .map() function is a powerful way to apply a function to every example in the dataset.
processed_dataset = dataset.map(
    preprocess_function,
    batched=True,
)

print("✅ Dataset has been processed and is ready for the trainer.")