# Run the main method
# change output directory to desired path on your machine

## Output directory
#dir = ""

## main method
#def main():
 


# Returns the picture given a directory
def getPic():
  return makePicture(pickAFile())

# Writes a picture to a file  
def writePict(pict,name):
  file=getMediaPath(name)
  writePictureTo(pict,file)

# Draw a snowman
def warmUp(pic):
  radius = 50
  x = getWidth(pic) / 5
  y = getHeight(pic) / 5
  for i in range(1,4):
    
    addOvalFilled(pic, x, y, radius, radius, white)
    
    y = y + radius - radius/4
    x = x - radius/2
    radius = radius * 2
    
  show(pic)
   
# the card canvas is a scene with 3 pumpkins with cutouts for faces
def drawCard(canvas):
  # Three pics below should be of faces to draw on cutouts
  pic1 = getPic()
  pic2 = getPic()
  pic3 = getPic()
  
  # Draws face on pumpkin 1
  drawFace(canvas, pic1, 181, 362, 241, 403)
  # Draws face on pumpkin 2
  drawFace(canvas, pic2, 371, 611, 352, 521)
  # Draws face on pumpkin 3
  drawFace(canvas, pic3, 628, 798, 266, 440)
  show(canvas)


def drawFace(canvas, face, x1, x2, y1, y2):
  holeWidth = abs(x1-x2)
  holeHeight = abs(y1-y2)
  faceWidth = getWidth(face)
  faceHeight = getHeight(face)
  

  widthRatio, heightRatio = 1
  
  # Check sizes of photos and resize if necessary
  # To do: Find out how to stretch or shrink by a non-integer amount
  # without running into errors
  # To do: Can we generalize a function (named resize) to shrink/stretch a photo
  # Rather than creating separate shrink/stretch functions?
  if(holeWidth > faceWidth):
    widthRatio = float(holeWidth/faceWidth)
    print widthRatio
    
  if(holeHeight > faceHeight):
    heightRaio = float(holeHeight/faceHeight)
    print heightRatio
  stretch(face, widthRatio, heightRatio)
  
# px and py are the x, y locations of the picture of a face
  px = 0
  py = 0
  
  for x in range(x1, x2):
    for y in range(y1, y2):
      # If the pixel in the canvas is white enough, draw the pixel
      # from the face picture. Otherwise, leave it alone!    
      if distance(getColor(getPixel(canvas, x, y)), white) < 100:
        setColor(getPixel(canvas, x, y), getColor(getPixel(face, px, py)))
      # Proceed to next y location of face picture  
      py = py + 1
        
    # When the inner loop is exited, increase the x location of face picture
    # And reset the y location of the face picture to 0
    px = px + 1
    py = 0
    
  #show(canvas)
  return canvas

def stretch(pic, widthRatio, heightRatio):
  w, h = getWidth(pic), getHeight(pic)
  canvas = makeEmptyPicture(w*widthRatio, h*heightRatio)  
  for x in range(0, getWidth(canvas)):
     for y in range(0, getHeight(canvas)):
        setColor(getPixel(canvas,x,y), getColor(getPixel(pic,x/widthRatio,y/heightRatio))) 
  #show(canvas)
  return canvas
   
        
  
  
  