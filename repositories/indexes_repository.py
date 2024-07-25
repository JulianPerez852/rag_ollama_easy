from langchain_community.document_loaders import PDFPlumberLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import warnings
warnings.filterwarnings("ignore")

class IndexesRepository:
    def create_indexes(self, path):

        print(f"Vectorizando {path}")

        loader = PDFPlumberLoader(path)
        docs = loader.load()

        text_splitter = SemanticChunker(HuggingFaceEmbeddings())
        documents = text_splitter.split_documents(docs)

        vector = FAISS.from_documents(documents, HuggingFaceEmbeddings())

        return vector
    
    def save_indexes(self, vector, path):
        vector.save_local(path)

    def load_indexes(self, path):
        print(path)
        return FAISS.load_local(path, HuggingFaceEmbeddings(), allow_dangerous_deserialization=True)

    def delete_indexes(self, path):
        pass

    def update_indexes(self, path):
        pass


