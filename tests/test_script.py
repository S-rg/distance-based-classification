import cv2
def check_images():
    try:
        tharoor = cv2.imread('img/Dr_Shashi_Tharoor.jpg')
        plaksha = cv2.imread('img\Plaksha_Faculty.jpg')

        if tharoor is None or plaksha is None:
            raise Exception
        
    except:
        print("File not found or unreadable")
