fileToOpen = input("Name of the file to open > ")
fileToCopy = input("Name of the file to output > ")
#Opens the file with "with"
with open(f"{fileToOpen}.txt", "r") as file:
     #Reads every line
     data = file.readlines()
     #All chars in lowercase
     data.sort(key=lambda y: y.lower())
     #Creates output file
     fileResult = open(f"{fileToCopy}.txt", "w")
     #Copies to output file
     for line in data:
          fileResult.write(line)