#  bildgenerator
#  Name:        image generator
#  Funktion:    wandle outputimage.txt in output.png um
#  @author Johannes Röring
#  @version 1.0.0 20/11/20
#  the following script was made for personal use, for questions and ideas please
#  feel free to contact me
#  contact: mail@jroering.com

from PIL import Image
#erstelle leeres bild 300x300px gross, hintergrundfarbe rot
im = Image.new("RGB",(300,300),"#FF0000")
row = 0
column = 0
value = 0
with open('outputImage.txt') as f:
  while True:
    c = f.read(1)
    if not c:
      break
    #print ("Read a character:", c)
    if (c=='\n'):
        row = row + 1
        column = 0
    else:
        if(c=='.'): value = 255
        if(c=='@'): value = 0
        im.putpixel((column,row),(value,value,value))
        column = column + 1 
im.show()
im.save('output.png')

