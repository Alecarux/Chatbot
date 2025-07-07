def preprocess_documents(data_path):
    # Per ora solo carica i file come testo semplice in una lista
    import os
    docs = []
    for filename in os.listdir(data_path):
        with open(os.path.join(data_path, filename), 'r', encoding='utf-8') as f:
            docs.append(f.read())
    return docs
#ciaooeao0rfdsi<okvocdkms
