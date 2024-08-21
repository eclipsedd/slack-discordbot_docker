# capable in: image interpretation, speech transcription, text summarisation

from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("model_name_or_path")
model = AutoModelForCausalLM.from_pretrained("model_name_or_path")


# Function to generate text
def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=50)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Example usage
prompt = "What is the capital of India?"
print(generate_text(prompt))
