from  april_detector_pywrapper import PyAprilTagDetector
import numpy as np
import cv2
import pdb

def main():
    img = cv2.imread("test.png")

    height,width,_ = img.shape

    fx = 600
    fy = 600
    cx = int(width/2)
    cy = int(height/2)
    tagSize = 0.025

    detector = PyAprilTagDetector()
    detector.setImageSize(width, height)
    detector.setCameraParams(fx, fy, cx, cy)
    detector.setTagSize(tagSize)
    detector.setTagCodes("36h9")
    detector.setup()
    detector.getDetectedInfo(img, draw_flag=True)
    taginfo_list = detector.extractTagInfo()
    res_img = detector.getDetectedImage()

    intrinsic_parameter_matrix = np.array([[fx,0,cx],[0,fy,cy],[0,0,1]])
    while cv2.waitKey(10)&0xFF != 27: 
        cv2.imshow("res_img", res_img)

    cv2.imwrite("res_img.png", res_img)
    cv2.waitKey(10)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
