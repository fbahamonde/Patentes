import cv2
import os
import DetectPlates
import base64
import json
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import Drawing as dr
import Correction as cor

showSteps = False


###################################################################################################
def main():
    imgOriginalScene  = cv2.imread("lejos.jpg")               # open image
    if imgOriginalScene is None:                            # if image was not read successfully
        print "\nerror: image not read from file \n\n"      # print error message to std out
        os.system("pause")                                  # pause so user can see error message
        return                                              # and exit program
    # end if
    listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           # detect plates
    cv2.imshow("imgOriginalScene", imgOriginalScene)            # show scene image

    if len(listOfPossiblePlates) == 0:                          # if no plates were found
        print "\nno license plates were detected\n"             # inform user no plates were found
    else:                                                       # else
                # if we get in here list of possible plates has at leat one plate

                # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
        listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

                # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
        licPlate = listOfPossiblePlates[0]
        recorte=licPlate.imgPlate
        cv2.imwrite("recorte.png", recorte) 
		
        credentials = GoogleCredentials.get_application_default()
        service = discovery.build('vision', 'v1', credentials=credentials)
        with open('recorte.png', 'rb') as image:
            image_content = base64.b64encode(image.read())
            service_request = service.images().annotate(body={
                    'requests': [{
                            'image': {
                                    'content': image_content.decode('UTF-8')
                                    },
                            'features': [{
                                    'type': 'TEXT_DETECTION',
                                    'maxResults': 1    
                                    }]
                            }]
                            })
        response = service_request.execute()
        resultado=json.dumps(response['responses'][0]['fullTextAnnotation']['text'], indent=4, sort_keys=True)
        resultado=cor.remove_punctuation(resultado)
        print resultado

        dr.drawRedRectangleAroundPlate(imgOriginalScene, licPlate)             # draw red rectangle around plate
        dr.writeLicensePlateCharsOnImage(imgOriginalScene, licPlate,resultado)           # write license plate text on the image
        cv2.imshow("imgOriginalScene", imgOriginalScene)                # re-show scene image
        cv2.imwrite("imgOriginalScene.png", imgOriginalScene)           # write image out to file
        cv2.imshow("imgPlate", licPlate.imgPlate)           # show crop of plate and threshold of plate
    cv2.waitKey(0)					# hold windows open until user presses a key

    return

if __name__ == "__main__":
    main()

