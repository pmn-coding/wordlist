namen =  ['Thomas','Susanne','Anne','Hans'] 
for  text  in  namen: 
   print('Der Name ',text,' besteht aus ',len(text),' Buchstaben.')

# mit dem Befehl "append" können weitere Listenelemente hinzugefügt werden

namen.append('Lisa')
print(namen)

# Ergänze das Programm, sodass in einem Eingabedialog weitere Namen
   # eingegeben werden.
while True:
   cc = input("Eingabe:")
   # Der Dialog wird duch die Eingabe des Wortes "Ende" beendet.
   if cc == "Ende" or "ende" or "Exit" or "exit":
      break
   else:
      namen.append(cc)

