import cv2
import numpy as np

image1 = cv2.Canny(cv2.cvtColor(cv2.imread("map1.jpg"), cv2.COLOR_BGR2GRAY),250 ,180)
image2 = cv2.Canny(cv2.cvtColor(cv2.imread("map10.png"), cv2.COLOR_BGR2GRAY),250,180)

h, w = image2.shape

metodlar = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

cv2.imshow("2.resim_canny_version",image2)
for metod in metodlar:
    image1_1 = image1.copy()

    sonuc = cv2.matchTemplate(image1_1,image2,metod)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(sonuc)
    
    if metod in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
        
        sag_alt = (location[0]+w,location[1]+h)
        cv2.rectangle(image1_1,location,sag_alt,255,5)
        cv2.imshow("cikti",image1_1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    

    