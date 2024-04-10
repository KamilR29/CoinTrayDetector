import numpy as np
import cv2 as cv

# Load the image
img = cv.imread('tray8.jpg', 0)

# Apply median blur for noise reduction
img = cv.medianBlur(img, 5)

# Convert image to color for visualization purposes
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

# Find edges using Canny edge detector
edges = cv.Canny(img, 50, 200, apertureSize=3, L2gradient=True)



# Find contours of the edges
contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Iterate through contours to find the tray contour
tray_contour = None
max_area = 0
for contour in contours:
    area = cv.contourArea(contour)
    if area >= max_area:
        max_area = area
        tray_contour = contour

# Draw the contour of the tray
cv.drawContours(cimg, [tray_contour], -1, (0, 255, 0), 2)


# Find circles using Hough transform
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 20, param1=100, param2=40, minRadius=20, maxRadius=70)

if circles is not None:
    circles = np.uint16(np.around(circles))

    # Initialize counters
    big_coins_tray = 0
    small_coins_tray = 0
    big_coins_out = 0
    small_coins_out = 0

    # Iterate through detected circles
    for i in circles[0, :]:
        # Check if the circle is inside the tray contour
        if cv.pointPolygonTest(tray_contour, (i[0], i[1]), False) >= 0:
            # Determine if it's a big or small coin based on radius
            if i[2] > 32:  # Adjust this threshold according to your images
                big_coins_tray += 1
            else:
                small_coins_tray += 1
        else:
            if i[2] > 32:  # Adjust this threshold according to your images
                big_coins_out += 1
            else:
                small_coins_out += 1

    print("Big coins in tray:", big_coins_tray)
    print("Small coins in tray:", small_coins_tray)
    print("Big coins out of tray:", big_coins_out)
    print("Small coins out of tray:", small_coins_out)

    # Draw detected circles
    for i in circles[0, :]:
        cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

# Display the result
cv.imshow('Result', cimg)
cv.waitKey(0)
cv.destroyAllWindows()
