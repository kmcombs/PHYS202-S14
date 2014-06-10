
class Blob():
    def __init__(blob):
        #Constructs and empty blob
        blob.pixels = []
    def add(blob, i , j):
        #add pixels i and j to blob
        blob.pixels.append((i,j))
    def mass(blob):
        #return number of pixels added
        mass = len(blob.pixels)
        return mass
    def centerOfMass(blob):
        #return (x,y) location of blob's center of mass
        #format with 4 digits to the right of the decimal point
        x = 0
        y = 0
        for loc in range(0, len(blob.pixels)):
            x += blob.pixels[loc][0]
            y += blob.pixels[loc][1]
        xcm = float(x)/float(len(blob.pixels))
        ycm = float(y)/float(len(blob.pixels))
        return ["%.4f" %xcm, "%.4f" %ycm]

def countBeads(P, blob_m):
    '''return the number of beads with >= P pixels'''
    i = 0
    for i in blob_m: #if the mass is greater than P the blob is a bead 
        if i >= P:
            i+= 1
    return i

def getBeads(P, blob_m, blob_cm):
    '''return all beads with >= P pixels'''
    bead_m = []
    bead_cm = []
    for i in range(len(blob_m)):
        if blob_m[i] >= P:
            bead_m.append(blob_m[i])
            bead_cm.append(blob_cm[i])
    return bead_m, bead_cm

def BlobFinder(pic, tau, P):
    """Input a list of picutures, a threshold value and the minimum size of the beads. The
    function will return the number of beads per frame, the masses of all the beads in every frame
    in a list, the coordinates of the center of mass of all the beads in every frame. It will also return
    the masses of all the blobs, that didn't meet the minimum bead size, in all the frames and the center 
    of mass cooridinates of all the blobs. 
    i, bead_m, bead_cm, blob_m, blob_cm = BlobFinder(pictures, threshold, minimum bead size)"""
    #scan the image top to bottom and left to right using a nested loop.
    #when black pixel is found, increment the count, then call the fill
    #function to fill in all the pixels connected to that one.
    blob1 = Blob() #call the class
    blob_cm = []
    blob_m = []
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    xsize, ysize = pic.size
    temp = pic.load()
    for x in range(xsize):
        for y in range(ysize):
            r,g,b = temp[x,y]
            if r+g+b >= tau: 
                temp[x,y] = WHITE
            else:
                temp[x,y] = BLACK
    #keep a list of pixels that need to be looked at, 
    #but haven't yet been filled in - a list of the (x,y) 
    #coordinates of pixels that are neighbors of ones we have 
    #already examined.  Keep looping until there's nothing 
    #left in this list
    for x in range(xsize):
        for y in range(ysize):
            if temp[x,y] == BLACK:
                blob1.__init__() #clears the blob.pixels list in the class
                                #now able to store new values
                queue = [(x,y)]
                while queue:
                    x,y,queue = queue[0][0], queue[0][1], queue[1:]
                    if temp[x,y] == BLACK:
                        temp[x,y] = RED
                        blob1.add(x,y) #if a pixel is red, add the coordinates
                                        #to the class
                        if x > 0:
                            queue.append((x-1,y))
                        if x < (xsize-1):
                            queue.append((x+1,y))
                        if y > 0:
                            queue.append((x, y-1))
                        if y < (ysize-1):
                            queue.append((x, y+1))
                blob_cm.append(blob1.centerOfMass()) #after all the blob's pixels
                                                    #are added, find the center of mass
                blob_m.append(blob1.mass()) #counts how many pixels are in a blob
    i = countBeads(P, blob_m) #finds how many blobs are beads
    bead_m, bead_cm = getBeads(P, blob_m, blob_cm) #finds the mass and center of mass 
                                                    #of all the blobs that are beads
    return i, bead_m, bead_cm, blob_m, blob_cm #returns the amount of beads, the mass and center
                                                #of mass of the beads, and the mass and center of
                                                #of mass of all the blobs.
