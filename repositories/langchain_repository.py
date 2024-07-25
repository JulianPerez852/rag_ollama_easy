from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings

class LangchainRepository:

    def load_model(self, model_name):
        llm = Ollama(model=model_name)
        return llm
    
    def create_retriever(self, vector, k):
        retriever = vector.as_retriever(search_type="similarity", search_kwargs={"k": k})
        return retriever

    def create_prompt(self, prompt, llm):

        QA_CHAIN_PROMPT = PromptTemplate.from_template(prompt) 
        llm_chain = LLMChain(
                        llm=llm, 
                        prompt=QA_CHAIN_PROMPT, 
                        callbacks=None, 
                        verbose=True)
        return llm_chain
    
    def create_qa_chain(self, llm_chain, retriever):
        
        document_prompt = PromptTemplate(
            input_variables=["page_content", "source"],
            template="Context:\ncontent:{page_content}\nsource:{source}",
        )

        combine_documents_chain = StuffDocumentsChain(
                        llm_chain=llm_chain,
                        document_variable_name="context",
                        document_prompt=document_prompt,
                        callbacks=None,
                    )

        qa = RetrievalQA(
                        combine_documents_chain=combine_documents_chain,
                        verbose=True,
                        retriever=retriever,
                        return_source_documents=True,
                    )
        
        return qa