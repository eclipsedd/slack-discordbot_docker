from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from accelerate import Accelerator
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

# Ensure the model is downloaded and available locally
model_name = "meta-llama/Meta-Llama-3-8B-Instruct"

# Initialize the tokenizer and model from local files
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

accelerator = Accelerator()

model, tokenizer = accelerator.prepare(model, tokenizer)

# Initialize the text generation pipeline
text_generation_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=accelerator.device.index,
    framework="pt",
)


def generate_response(user_text, max_length=200):
    prompt = f"Q: {user_text}\nA:"
    try:
        with accelerator.device_placement():
            response = text_generation_pipeline(
                prompt, max_length=max_length, num_return_sequences=1
            )
        return response[0]["generated_text"].strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't generate any response."


# Example usage
if __name__ == "__main__":
    user_input = "What is the capital of France?"
    response = generate_response(user_input)
    print(response)
