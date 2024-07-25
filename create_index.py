import os
from services.indexes_manager_service import IndexesManagerService
from repositories.indexes_repository import IndexesRepository

def run_create_index(path, name):

    service = IndexesManagerService(IndexesRepository())

    if path != "data":
        index = service.create_index(path)
        service.save_index(index, name)
    else:
        print(f"\033[92m Servicio no disponible aún ___________"
              f"\U0001F995 \U0001F995 \U0001F995 \U0001F995 \033[0m___________")



if __name__ == "__main__":
    path_data = 'data'
    pdf_files = []

    for num, file in enumerate(os.listdir(path_data)):
        if file.endswith(".pdf"):
            pdf_files.append(str(num) + ". " + file)

    list_files = "\n".join(pdf_files)
    file_choose = input(f"Escoge cual PDF es el que quieres vectorizar, escribe el numero que le"
                        f"corresponde a cada PDF \n-1. Todos\n{list_files}\n \033[91m___________________________ \n")

    name = input("\033[0mEscribe el nombre del index: \n \033[91m___________________________ \n")

    if file_choose == "-1":
        run_create_index(path_data, name)
    else:
        run_create_index(path_data + '/' + pdf_files[int(file_choose) -1 ].split(". ")[1], name)