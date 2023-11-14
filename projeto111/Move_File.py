import os
import shutil

from_dir = "C:/Users/Family/Downloads"
to_dir = "C:/Users/Family/OneDrive/Área de Trabalho/ESTUDOS/BYJUS/vs code"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    # print(name, extension)

print("Saída obtida!")

