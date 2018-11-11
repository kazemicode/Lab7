# Run the main method
# change output directory to desired path on your machine

## Output directory
dir = ""

## main method
def main():
  writePict(removeRedEye(getPic(), 322, 995, 385, 465), dir + "/noredeye.jpg")
  writePict(sepia(getPic()), dir + "/sepia.jpg")
  writePict(artify(getPic()), dir + "/artify2.jpg")
  writePict(chromaKey(getPic(), getPic()), dir + "/greenscreen2.png")


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
   
def thanks(canvas):
  pic1 = getPic()
  pic2 = getPic()
  pic3 = getPic()
  drawFace(canvas, pic1, 181, 362, 241, 403)
  drawFace(canvas, pic2, 371, 611, 352, 521)
  drawFace(canvas, pic3, 628, 798, 266, 440)
  show(canvas)

#pumpkin 1: drawFace(181, 362, 241, 403)
#pumpkin 2: drawFace(372, 611, 352, 521)
#pumpkin 3: drawFace(628, 798, 266, 440)
def drawFace(canvas, face, x1, x2, y1, y2):
  holeWidth = abs(x1-x2)
  holeHeight = abs(y1-y2)
  faceWidth = getWidth(face)
  faceHeight = getHeight(face)
  
# Check sizes of photos and resize if necessary
  widthRatio = 1
  heightRatio = 1
  
  if(holeWidth > faceWidth):
    widthRatio = float(holeWidth/faceWidth)
    print widthRatio
    
  if(holeHeight > faceHeight):
    heightRaio = float(holeHeight/faceHeight)
    print heightRatio
  stretch(face, widthRatio, heightRatio)
  

  px = 0
  py = 0
  
  for x in range(x1, x2):
    for y in range(y1, y2):
      if distance(getColor(getPixel(canvas, x, y)), white) < 100:
        setColor(getPixel(canvas, x, y), getColor(getPixel(face, px, py)))
        
      py = py + 1
        
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
  show(canvas)
   
        
  
  
  