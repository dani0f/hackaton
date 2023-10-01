from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from read_files import load_files

def query(query):
    tokenizer = AutoTokenizer.from_pretrained("model")
    model = AutoModel.from_pretrained("model")
    documents = load_files('dataset')
    # Estos dos pasos siguientes se pueden pasar a otra función para hacer una base de datos de los embeddings de documentos
    # Preprocess and encode documents
    encoded_documents = []
    for doc in documents:
        encoded_input = tokenizer.encode_plus(
            doc,
            add_special_tokens=True,
            truncation=True,
            max_length=128,
            padding='max_length',
            return_tensors='pt'
        )
        encoded_documents.append(encoded_input)

    # Create document embeddings using BERT
    document_embeddings = []
    with torch.no_grad():
        for encoded_doc in encoded_documents:
            input_ids = encoded_doc['input_ids']
            attention_mask = encoded_doc['attention_mask']
            outputs = model(input_ids, attention_mask=attention_mask)
            doc_embedding = torch.mean(outputs.last_hidden_state, dim=1).squeeze()
            document_embeddings.append(doc_embedding)


    # Preprocess and encode the search query
    encoded_query = tokenizer.encode_plus(
        query,
        add_special_tokens=True,
        truncation=True,
        max_length=128,
        padding='max_length',
        return_tensors='pt'
    )

    # Compute query embedding
    with torch.no_grad():
        input_ids = encoded_query['input_ids']
        attention_mask = encoded_query['attention_mask']
        outputs = model(input_ids, attention_mask=attention_mask)
        query_embedding = torch.mean(outputs.last_hidden_state, dim=1).squeeze()
    similarity_scores = cosine_similarity(query_embedding.unsqueeze(0).numpy(), np.stack(document_embeddings))
    k = 5  
    top_k_indices = np.argsort(similarity_scores, axis=1)[0][-k:][::-1]

    # Retrieve the top-k most similar documents
    top_k_documents = [documents[i] for i in top_k_indices]
    return top_k_documents

result = query("incendio")
for i in result:
    print(i[:50])