# Dette er et lille program som ligner en lille wordproccessor koden er kun på knap 14 linier.
# Skrevet af Frank Simens efter instpiration af bogen automate stuff
# programmer kan bruges til flere tekstfiler efter hinanden. Kontakt frank@simens.dk version python 3.8

from pathlib import Path                                    # installer pathlip med pip
filename = input('Hvad skal filen hedde? ')                 # filename er hvad filen skal hedde det bliver brugeren spurgt om
p = Path(filename)                                          # set var p til filename also brugerinput.
text = input('Indtast her den tekst der skal skrives: \n')  # set var text til input af den tekst der skal
                                                            # skrives i textfilen. genstart programmet for at gemme flere filer
                                                            # i samme mappe
p.write_text(text)                                          # Skriv filen til disken, efter filname
file = p.read_text()                                        # set var file til at hente tekst fra fil som kvittering.
print (file)                                                # vis tekstfilen i promt.
