from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/multi-qa-mpnet-base-dot-v1")
model = AutoModel.from_pretrained("sentence-transformers/multi-qa-mpnet-base-dot-v1")
tokenizer.save_pretrained("model")
model.save_pretrained("model")