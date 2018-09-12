# Main.py
# module level variables ##########################################################################
showSteps = True
import cv2
import os
import DetectChars
import DetectPlates
import Drawing as dr
import time
time1=''
guarda=os.listdir('C:\Users\FelipeBahamonde\Desktop\proyecto patentes\Aprendizaje de maquinas\ejemplo martes')
cantidad=len(guarda)


DetectChars.loadKNNDataAndTrainKNN()
SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)
#%%
def main():
    for i in range(1):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        imgOriginalScene  = cv2.imread("ejemplo martes/"+guarda[i])           
        if imgOriginalScene is None:                            
            print "\nerror: image not read from file \n\n"     
            os.system("pause")                                 
            return             
        height, width, numChannels = imgOriginalScene.shape
        X=800/(width*1.0)
        imgOriginalScene = cv2.resize(imgOriginalScene, (0,0), fx=X, fy=X)
        
        listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           # detect plates
        listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)        # detect chars in plates
        if len(listOfPossiblePlates) == 0:
            print "\nno No detectaron posibles patentes\n"             # inform user no plates were found
        else:                                                       # else
            listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)
            licPlate = listOfPossiblePlates[0]
            recorte=licPlate.imgPlate
            cv2.imwrite("recorte patente/"+timestr+".png", recorte)

            if len(licPlate.strChars) == 0:                     # if no chars were found in the plate
                  print "\nno characters were detected i possible plate\n\n"       # show message
                  return                                          # and exit program
            try:
                print "\nlicense plate read from image = " + licPlate.strChars + "\n"       # write license plate text to std out
                print "----------------------------------------"
                resultado=licPlate.strChars
                dr.drawRedRectangleAroundPlate(imgOriginalScene, licPlate)             # draw red rectangle around plate
                dr.writeLicensePlateCharsOnImage(imgOriginalScene, licPlate,resultado)           # write license plate text on the image
                cv2.imwrite("captura auto/"+timestr+".png", imgOriginalScene)           # write image out to file
            except Exception:
                print Exception
                print "No se encontraron patentes"
            dr.drawRedRectangleAroundPlate(imgOriginalScene, licPlate)             # draw red rectangle around plate
            cv2.imwrite("imgOriginalScene.png", imgOriginalScene)           # write image out to file      
            time.sleep(2)
    return

if __name__ == "__main__":
    main()



