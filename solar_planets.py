import cv2

img =  cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sun",
            (20, 230),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255, 255, 255)
            )
cv2.putText(img,
            "Mercury",
            (110, 180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Venus",
            (190, 280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Earth",
            (290, 280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Mars",
            (380, 280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Jupiter",
            (590, 400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Saturn",
            (770, 310),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Uranus",
            (970, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.putText(img,
            "Neptune",
            (1111, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.imshow("Solar System",img)
cv2.waitKey(0)
cv2.imwrite('Solar_system.jpg',img)