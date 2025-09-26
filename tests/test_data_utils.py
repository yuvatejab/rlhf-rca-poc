import pandas as pd

# --- 1. Define Test Prompts ---

test_prompts = [
    {"prompt": "Provide a Root Cause Analysis for the recent API latency spike."},
    {"prompt": "Provide a Root Cause Analysis for the recent database connection failure."},
    {"prompt": "Provide a Root Cause Analysis for the recent user login outage."},
]


print("--- Generating with Original Model (Before RLHF) ---")
original_results = []
for item in test_prompts:
 
    input_ids = tokenizer(item["prompt"], return_tensors="pt").input_ids
    
   
    generation_output = original_model.generate(
        input_ids=input_ids,
        **generation_kwargs
    )
    response_text = tokenizer.decode(generation_output[0], skip_special_tokens=True)
    
   
    score_text = item["prompt"] + response_text
    inputs = tokenizer(score_text, return_tensors="pt").to(reward_model.device)
    output = reward_model(**inputs)
    score = output.logits[0].item()
    
    original_results.append({"prompt": item["prompt"], "response": response_text, "score": score})


print("\n--- Generating with Fine-Tuned Model (After RLHF) ---")
ppo_results = []
for item in test_prompts:
   
    input_ids = tokenizer(item["prompt"], return_tensors="pt").input_ids
    

    generation_output = ppo_model.generate(
        input_ids=input_ids,
        **generation_kwargs
    )
    response_text = tokenizer.decode(generation_output[0], skip_special_tokens=True)
    

    score_text = item["prompt"] + response_text
    inputs = tokenizer(score_text, return_tensors="pt").to(reward_model.device)
    output = reward_model(**inputs)
    score = output.logits[0].item()
    
    ppo_results.append({"prompt": item["prompt"], "response": response_text, "score": score})



print("\n\n--- Comparison of Model Outputs ---")
df_original = pd.DataFrame(original_results)
df_ppo = pd.DataFrame(ppo_results)


df_comparison = pd.DataFrame({
    'Prompt': df_original['prompt'],
    'Response (Before RLHF)': df_original['response'],
    'Score (Before)': df_original['score'].round(2),
    'Response (After RLHF)': df_ppo['response'],
    'Score (After)': df_ppo['score'].round(2)
})


display(df_comparison)


avg_score_original = df_original['score'].mean()
avg_score_ppo = df_ppo['score'].mean()

print(f"\nAverage Reward Score (Before RLHF): {avg_score_original:.2f}")
print(f"Average Reward Score (After RLHF):  {avg_score_ppo:.2f}")
