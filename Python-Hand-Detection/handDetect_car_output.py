import cv2
import numpy as np
import imutils
import math

def detect_hands(img):  
    hand = cv2.CascadeClassifier('palm.xml') #Cascade Classifier for front-facing hands
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converts image to grayscale
    hands = hand.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) #All detected hands get put into an array
    if len(hands) != 0:        
        return hands
    else:
        return False

def getAngle(x,y,x2,y2):
    ''' a1
        /|
       / |
      /__|
    a3   a2
    '''
    a1 = [x2,y2] #Center of hand
    a2 = [x2,(y2+((y/2)-y2))] #x axis of the center frame and y axis of the hand center, forms a right angle
    a3 = [x/2,y/2] #Center of frame

    hypot = math.hypot(a1[0]-a3[0],a1[1]-a3[1]) #distance between the frame center and hand center
    ydistance = math.hypot(a1[0]-a2[0],a1[1]-a2[1]) #distance between the hand center and the right angle 
    angle = math.degrees(math.asin(ydistance/hypot)) #angle from the hand center to the frame center

    #Draws a right triangle on the frame
    #points = np.array([a1,a2,a3])
    #cv2.polylines(img,np.int32([points]),1,(0,0,255))


    #Angles currently used are for dispalying the car image with forward/backward movement
    #Use the uncommented lines in the bottom half section for full 360 degree output

    #Top half of plane
    if y2 < y/2:
        direction1 = "forward"
        if x2 > x/2: #Quadrant 1
            direction2 = "right"
            angle = angle
        elif x2 < x/2: #Quadrant 2
            direction2 = "left"
            angle = 180 - angle

    #Bottom half of plane
    elif y2 > y/2:
        direction1 = "backward"
        if x2 < x/2: #Quadrant 3
            direction2 = "left"
            #angle = 180 + angle #Use for an exact degree, will be between 180 and 270
            angle = angle
        elif x2 > x/2: #Quadrant 4
            direction2 = "right"
            #angle = 360 - angle #Use for an exact degree, will be between 270 and 360
            angle = 180 - angle
    
    return int(angle), direction1, direction2

forwardcar = cv2.imread('./forwardcar.png')
backwardcar = cv2.imread('./backwardcar.png')
camera = cv2.VideoCapture(0) #Detects webcamera

#Sets frame size to small for quicker processing
camera.set(cv2.CAP_PROP_FRAME_WIDTH,100);
camera.set(cv2.CAP_PROP_FRAME_HEIGHT,100);

camera.set(cv2.CAP_PROP_FPS,60);
    
while camera.isOpened():

    ret, frame = camera.read()
    y,x,_ = frame.shape
    
    frame = cv2.bilateralFilter(frame, 9, 0, 0)  #Smoothing filter
    img = cv2.flip(frame, 1) #Flips the frame horizontally
    hands = detect_hands(img) #Array of coordiantes where hands are located
    
    try:
        #Grid pattern drawn
        cv2.line(img,(int(x/2),0),(int(x/2),y),(0,0,0),1)
        cv2.line(img,(0,int(y/2)),(x,int(y/2)),(0,0,0),1)
        cv2.imshow('frame',img) #Show grid and frame

        if hands.any():

            for (a,b,w,h) in hands:
                x2, y2 = (int(a+(w/2)),int(b+(h/2))) #Center coords of the hand
                angle, direction1, direction2 = getAngle(x,y,x2,y2) #Returns angle from center of frame to center of hand

                #Set the car image to use, based on the position of the hand
                if direction1 == 'forward':
                    car = forwardcar
                else:
                    car = backwardcar

                car_img = imutils.rotate_bound(car,-angle) #Adjust car image to appropriate angle 
                cv2.line(img,(int(x/2),int(y/2)),(x2,y2),(0,255,0),3) #Line to center of hand from center of frame
                
                print('\n\nMoving '+direction1+' and '+direction2)
                
            cv2.imshow('car',car_img) #Show rotated car
            cv2.imshow('frame',img) #Show line to center of hand

            
    except:
        #If no hands were detected nothing happens
        pass
    
    k = cv2.waitKey(10) & 0xff #Detects key presses
    if k == 27:
        #If the esc key is pressed, stop the program
        break

#Required for continous recording
camera.release()
cv2.destroyAllWindows()

