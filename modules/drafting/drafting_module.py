from transformers import GPT2LMHeadModel, GPT2Tokenizer

class DraftingModule:

    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')

    def generate_draft(self, input_text):
        inputs = self.tokenizer.encode(input_text, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=150, num_return_sequences=1)
        draft = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return draft
