from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("lmsys/vicuna-13b-delta-v1.1")

model = AutoModelForCausalLM.from_pretrained("lmsys/vicuna-13b-delta-v1.1")

def generate(text):
  tokens = tokenizer(text)
  output = model(tokens)
  return output
  
