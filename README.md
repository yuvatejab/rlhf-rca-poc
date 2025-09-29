# RLHF Proof-of-Concept: Improving RCA Generation

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Transformers%20%7C%20TRL-yellow)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange.svg)

This repository contains an end-to-end proof-of-concept (POC) demonstrating how to use Reinforcement Learning from Human Feedback (RLHF) to align a small language model's outputs to a desired style. The specific task is to fine-tune `distilgpt2` to generate clearer and more effective Root Cause Analysis (RCA) statements.

This project was completed as part of an assessment with a 24-hour turnaround time, emphasizing rapid prototyping and a clear demonstration of the core RLHF loop.

***

## Project Scope & Expectations

* **Scope**: Implement a simplified feedback loop with RLHF.
* **Instructions**:
    1.  Use synthetic 👍/👎 feedback on RCA/hypothesis statements.
    2.  Train a simple reward model based on this feedback.
    3.  Use the reward model to fine-tune the base generator model with PPO.
    4.  Demonstrate and evaluate the model's improvement.
* **Expectations**:
    * A functional Python POC in a well-structured repository.
    * A training notebook demonstrating the end-to-end process.
    * Clear evaluation metrics for the models before and after training.
    * Documentation covering setup, design choices, and trade-offs.

***


# RLHF Proof-of-Concept: Improving RCA Generation

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Transformers%20%7C%20TRL-yellow)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange.svg)

This repository contains an end-to-end proof-of-concept (POC) demonstrating how to use Reinforcement Learning from Human Feedback (RLHF) to align a small language model's outputs to a desired style. The specific task is to fine-tune `distilgpt2` to generate clearer and more effective Root Cause Analysis (RCA) statements.

This project was completed as part of an assessment with a 24-hour turnaround time, emphasizing rapid prototyping and a clear demonstration of the core RLHF loop.

##  Project Demo

For a complete walkthrough of the project, the code, and the results, please view the short video demo:

**[ Watch the 5-Minute Loom Demo Here]** *(<- Link to your recorded demo)*

***

##  Project Scope & Expectations

* **Scope**: Implement a simplified feedback loop with RLHF.
* **Instructions**:
    1.  Use synthetic 👍/👎 feedback on RCA/hypothesis statements.
    2.  Train a simple reward model based on this feedback.
    3.  Use the reward model to fine-tune the base generator model with PPO.
    4.  Demonstrate and evaluate the model's improvement.
* **Expectations**:
    * A functional Python POC in a well-structured repository.
    * A training notebook demonstrating the end-to-end process.
    * Clear evaluation metrics for the models before and after training.
    * Documentation covering setup, design choices, and trade-offs.

***

##  Project Structure

The repository is organized to separate experimental code from reusable application logic.

rlhf-rca-poc/
│
├── app/
│   ├── data_utils.py           # Logic for generating synthetic data
│   └── ...                     # Other utility scripts
│
├── docker/
│   ├── Dockerfile              # Instructions to build a runnable container
│   └── requirements.txt        # Project dependencies
│
├── notebooks/
│   └── 1_reward_model_training.ipynb # Main notebook with the end-to-end workflow
│
├── reward_model_checkpoints/
│   └── ...                     # Saved weights of the trained reward model
│
└── README.md                   # This documentation


***

## 🛠️ Setup and Installation

To run this project locally, please follow these steps.

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    cd rlhf-rca-poc
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    # Create the environment
    python -m venv venv

    # Activate it (macOS/Linux)
    source venv/bin/activate

    # Or activate it (Windows)
    # venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    The exact library versions are crucial. Install them from the `requirements.txt` file.
    ```bash
    pip install -r docker/requirements.txt
    ```

## How to Run

The entire end-to-end process is contained within a single Jupyter Notebook.

1.  Launch VS Code or Jupyter Notebook from your activated virtual environment.
2.  Open the main notebook: `notebooks/1_reward_model_training.ipynb`.
3.  Select the `venv` virtual environment as your notebook kernel.
4.  Run all the cells from top to bottom to execute the full training and evaluation pipeline.

***

## Methodology & Design Choices

The core of this project is a three-phase RLHF pipeline:

1.  **Phase 1: Synthetic Data Generation**: To meet the 24-hour deadline, we generated synthetic data instead of using human labelers. A "good" RCA was defined as a clear, conclusive statement (e.g., "The root cause was... resolved by..."), while a "bad" RCA was vague and inconclusive (e.g., "It is unclear..."). This provided a strong, clean signal for the reward model.

2.  **Phase 2: Reward Model (RM) Training**: We fine-tuned a `distilgpt2` model for sequence classification on our synthetic pairs. Its sole job was to learn to assign a higher score to the "good" RCAs than the "bad" ones.

3.  **Phase 3: PPO Fine-Tuning**: We used the trained reward model as a "judge" in a reinforcement learning loop. The original `distilgpt2` model would generate RCAs, the reward model would score them, and the Proximal Policy Optimization (PPO) algorithm would update the generator to maximize the scores.

### Trade-offs

* **Model Choice**: We used `distilgpt2` instead of a larger, more capable model. This was a deliberate choice to ensure fast training and iteration within the POC's time constraints. The trade-off is that the model's baseline generative ability is limited.
* **Data Simplicity**: The synthetic data was based on simple templates. This makes it easy for the reward model to learn but risks the model overfitting to keywords rather than learning the concept of a "good RCA."

***

## 

Results & Evaluation

Clear metrics were used to evaluate the performance at each stage.

### Reward Model Performance

The reward model was evaluated on its ability to correctly classify unseen "chosen" vs. "rejected" pairs.

| Step | Training Loss | Validation Loss | Accuracy |
|:----:|:-------------:|:---------------:|:--------:|
| 50   | 0.127000      | 0.207177        | 0.955    |
| 100  | 0.200200      | 0.129633        | 0.945    |
| ...  | ...           | ...             | ...      |
| 550  | 0.080300      | 0.147666        | 0.965    |
| 600  | 0.214200      | 0.146505        | 0.950    |

**Conclusion:** The reward model achieved **~96% accuracy** on the validation set. This is an excellent result and confirms that our "judge" successfully learned the preferences defined in our synthetic data.


### Generator Model Improvement (Before vs. After)

The primary goal was to see if the PPO-tuned model produced better RCAs. The results were surprising.

| Prompt                                                             | Response (Before RLHF)                                                                                                                                                                                            | Score (Before) | Response (After RLHF)                                                                                                                                                                                  | Score (After) |
|:-------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------:|
| Provide a Root Cause Analysis for the recent API latency spike.    | ...http://www.boostfire.net/app/2012/10/national-research-fire-training-poster...                                                                                                                                  | -3.70          | ...The reason Cave››s authors disabled the ACS API caching graph in a major rewrite is because it could fill in extra memory...                                                                      | -5.35         |
| Provide a Root Cause Analysis for the recent database connection failure. | ...Root Cause Analysis and other systems are not a complete match for the normalized Root Cause Leadership Technologies...                                                                                      | -2.13          | ...That said, there is still a lot to learn about the programming language. SP, a type system known for recursion, proton statistics...                                                                    | -5.03         |
| Provide a Root Cause Analysis for the recent user login outage.    | ...The Wikimedia Foundation has posted an update on the service and the process, which can be viewed here...                                                                                                        | -5.84          | ...Protect your account after the outage and return the common input messages. When Uninstaller Description: Disable Root Applications...                                                                     | -5.36         |

