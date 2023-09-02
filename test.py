from transformers import LlamaForCausalLM, LlamaTokenizer

model_name = "WizardLM/WizardCoder-Python-34B-V1.0"
# model_name = "/root/codellama/34b-python-hf"
model = LlamaForCausalLM.from_pretrained(
    model_name,
    device_map="auto"
)

tokenizer = LlamaTokenizer.from_pretrained(model_name)
tokenizer.add_special_tokens(
            {

                "pad_token": "[PAD]",
            }
        )


print(tokenizer.encode("[PAD]"))
print(tokenizer.pad_token)
print(tokenizer.pad_token_id)
print(tokenizer.decode([1, 32000]))
print(tokenizer.bos_token)
print(tokenizer.bos_token_id)