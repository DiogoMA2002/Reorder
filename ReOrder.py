fileToOpen = input("Nome do ficheiro a abrir > ")
fileToCopy = input("Nome do ficheiro de saida > ")
#Abre o ficheiro com with(Facilita o codigo)
with open(f"{fileToOpen}.txt", "r") as file:
     #Le todas as linhas
     data = file.readlines()
     #ignora lowercase ao ordenar
     data.sort(key=lambda y: y.lower())
     #cria ficheiro out
     fileResult = open(f"{fileToCopy}.txt", "w")
     #copia tudo
     for line in data:
          fileResult.write(line)