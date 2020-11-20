#  textkonverter vorformatierung
#  Name:        vorformatierung
#  Funktion:    entfernt tabzeichen aus input.txt datei und speichert diese als input1.txt wieder ab
#  @author Johannes Röring
#  @version 1.0.0 20/11/20
#  the following scripts will all be documented in german,
#  for international use as well as translations and questions,
#  feel free to contact me
#  contact: mail@jroering.com

#öffne die textdatei input.txt, das 'r' steht für read only
textInput = open('input.txt', 'r')

#öffne und erstelle die textdatei input1.txt, welche dannach zu input umbenannt wird (im cmd script), das 'a' steht für append (zeilenweise addieren)
textOutput = open('input1.txt', 'a')
textOutput.truncate(0)

#laufe über jede zeile und lade die jeweilige in line
for line in textInput: 
    line = line.strip()             #entferne zusatzzeichen wie newline und carriage return \n \r \l etc.
    line = line.replaye('\t',''):   #ersetze tabzeichen gegen nicht (lösche tabs)   
    textOutput.write(line+'\n')  #speichere die bearbeitete zeile und füge newline character hinzu (\n)

#schliesse eingabedatei und ausgabedatei
textInput.close() 
textOutput.close()

