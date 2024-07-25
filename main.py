import gradio as gr
import os
from services.indexes_manager_service import IndexesManagerService
from services.langchain_manager_service import LangchainManagerService
from repositories.indexes_repository import IndexesRepository
from repositories.langchain_repository import LangchainRepository

from dotenv import load_dotenv

def create_qa_retreiver(path):

    PROMPT_TEMPLATE = os.getenv('PROMPT_TEMPLATE')
    LLM_NAME = os.getenv('LLM_NAME')
    VECTOR_QUANTITY = os.getenv('VECTOR_QUANTITY')

    #PROMPT_TEMPLATE = "1. Use the following pieces of context to answer the question at the end.\n2. If you don't know the answer, just say that \"No sé la respuesta\" but don't make up an answer on your own.\n3. Keep the answer crisp and limited to 3,4 sentences.\nContext: {context}\nQuestion: {question}\nHelpful Answer:"

    print(PROMPT_TEMPLATE)

    index_service = IndexesManagerService(IndexesRepository())
    vector = index_service.load_index(path)

    service_langchain = LangchainManagerService(LangchainRepository())
    llm = service_langchain.load_model(LLM_NAME)
    retriever = service_langchain.create_retriever(vector, int(VECTOR_QUANTITY))
    llm_chain = service_langchain.create_prompt(PROMPT_TEMPLATE, llm)
    qa_chain = service_langchain.create_qa_chain(llm_chain, retriever)

    return qa_chain

def respond(question,history):
    return qa(question)["result"]

if __name__ == "__main__":

    load_dotenv()

    path_index = 'indexes'
    indexes_files = []

    for num, file in enumerate(os.listdir(path_index)):
        indexes_files.append(str(num) + ". " + file)

    list_indexes = "\n".join(indexes_files)
    file_choose = input(f"Escoge cual indice quieres utilizar, escribe el numero que le "
                        f"corresponde a cada indice \n{list_indexes}\n \033[91m___________________________ \n")

    qa = create_qa_retreiver(path_index + '/' + indexes_files[int(file_choose)].split(". ")[1])

    gr.ChatInterface(
        respond,
        chatbot=gr.Chatbot(height=500),
        textbox=gr.Textbox(placeholder=f"Hazme una pregunta acerca de {indexes_files[int(file_choose)].split('. ')[1]}", container=False, scale=7),
        title=f"{indexes_files[int(file_choose)].split('. ')[1]} Chatbot",
        cache_examples=True,
        retry_btn=None,
    ).launch(share = True)