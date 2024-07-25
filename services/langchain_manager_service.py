from repositories.langchain_repository import LangchainRepository

class LangchainManagerService:

    def __init__(self, langchain_repository: LangchainRepository):
        self.langchain_manager = langchain_repository


    def load_model(self, model_name):
        return self.langchain_manager.load_model(model_name)

    def create_retriever(self, vector, k):
        return self.langchain_manager.create_retriever(vector, k)

    def create_prompt(self, prompt, llm):
        return self.langchain_manager.create_prompt(prompt, llm)

    def create_qa_chain(self, llm_chain, retriever):
        return self.langchain_manager.create_qa_chain(
            llm_chain, 
            retriever,
        )