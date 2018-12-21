import cv2
import numpy as np

#Open a simple image
i = "WhatsApp Image 2018-12-09 at 20.18.54.jpeg"
img=cv2.imread(i)

#converting from gbr to hsv color space
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#skin color range for hsv color space 
HSV_mask = cv2.inRange(img_HSV, (10, 15, 10), (17,170,255)) 
#HSV_mask = cv2.inRange(img_HSV, (0, 20, 0), (20,190,255)) 
HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
HSV_mask = 255-HSV_mask

#converting from gbr to YCbCr color space
img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
#skin color range for hsv color space 
YCrCb_mask = cv2.inRange(img_YCrCb, (10, 135, 85), (255,180,135)) 
#YCrCb_mask = cv2.inRange(img_YCrCb, (0, 115, 65), (255,160,115)) 
YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
YCrCb_mask = 255-YCrCb_mask

#merge skin detection (YCbCr and hsv)
global_mask = cv2.bitwise_and(YCrCb_mask,HSV_mask)
global_mask = cv2.medianBlur(global_mask,3)
global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4), np.uint8))
global_mask = 255-global_mask


HSV_result = cv2.bitwise_not(HSV_mask)
YCrCb_result = cv2.bitwise_not(YCrCb_mask)
global_result=cv2.bitwise_not(global_mask)



#show results
#cv2.imshow("1_HSV.jpg",HSV_result)
# cv2.imshow("2_YCbCr.jpg",YCrCb_result)
# cv2.imshow("3_global_result.jpg",global_result)
# cv2.imshow("Image.jpg",img)
cv2.imwrite("out-"+ i ,HSV_result)
cv2.imwrite("out1-"+ i ,YCrCb_result)
cv2.imwrite("out2-"+ i ,global_result)
#cv2.waitKey(0)
#cv2.destroyAllWindows() 


