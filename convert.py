#  textkonverter text zu anleitung
#  Name:        convert
#  Funktion:    wandele zeilenweise zu schwarzer und weisser masche um, und schreibe die output.txt
#  @author Johannes Röring
#  @version 1.0.0 20/11/20
#  the following script was made for personal use, for questions and ideas please
#  feel free to contact me
#  contact: mail@jroering.com
 
   
def handleline(stringText):
    word = stringText
    n=1
    length=""
    for val in range(1,len(word)):
        if word[val-1]==word[val]:
            n+=1
        else :
            length += word[val-1] + str(n) + ", "
            n=1
        #length += ("and "+word[i]+" repeats "+str(n))
    length += (word[val]+str(n)+", ")

    #print (length)  
    return length
    
def printImageFile (stringText):
    textOutputImage.write(stringText.replace("0",".").replace("1","@")+"\n")
    
    
# Opening input file in read only mode 
textInput = open('input.txt', 'r')

#opening / creating output files
textOutput = open('output.txt', 'a')
textOutputImage = open('outputImage.txt', 'a')
textOutput.truncate(0)
textOutputImage.truncate(0)

#counting lines
count = 0

# Using for loop 
for line in textInput: 
    count += 1
    line = line.strip()
    printImageFile(line)
    #gerade reihen (schwarz)
    if (count % 2)==0:
        colour = "S"
        line = line.replace("0","L").replace("1","R")
    #ungerade reihen (weiss)    
    else:
        colour = "W"
        line = line.replace("0","R").replace("1","L")
    
    #zeilenanfang schreiben
    prefix = "RR {} {}: ".format(count, colour)
    
    #gleiche maschen zählen, erste masche als R angeben
    line = handleline("R" + line )
    
    #textdatei schreiben, inklusive rva und zeilenende
    textOutput.write(prefix + line + "rva" + "\n") 

# Closing files 
textInput.close() 
textOutput.close()
