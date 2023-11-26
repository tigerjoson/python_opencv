import cv2 as cv
import numpy as np
#ref: chatgpt
#ref: https://learnopencv.com/cropping-an-image-using-opencv/
# Read the image
path =r'C:\Users\tiger\Downloads\401561329_870238287806140_5954039294289215665_n.jpg';
image = cv.imread(path)


# Variables to track the scaling factor
scaling_factor = 1.0
original_width = 0

def on_resize(event, x, y, flags, param):
    global scaling_factor, original_width

    if event == cv.EVENT_MOUSEWHEEL:
        # Get the mouse wheel delta
        delta = cv.getMouseWheelDelta(flags)

        # Update the scaling factor based on the mouse wheel movement
        scaling_factor *= 1.1 if delta > 0 else 0.9

        # Resize the window to maintain the original aspect ratio
        new_width = int(original_width * scaling_factor)
        cv.resizeWindow("Image Window", new_width, int(new_width / aspect_ratio))

        # Redraw the image
        cv.imshow("Image Window", image)

    elif event == cv.EVENT_LBUTTONDOWN:
        # Calculate the correct coordinates in the image
        image_x = int(x / scaling_factor)
        image_y = int(y / scaling_factor)
        print(f'x={image_x}')
        print(f'y={image_y}')
        #print("Image Coordinates: ({}, {})".format(image_x, image_y))
    



aspect_ratio = image.shape[1] / image.shape[0]  # Width / Height

# Get the original width of the image
original_width = image.shape[1]

# Create a window with the cv.WINDOW_KEEPRATIO flag
cv.namedWindow("Image Window", cv.WINDOW_KEEPRATIO)
cv.imshow("Image Window", image)

# Set the mouse callback function
cv.setMouseCallback("Image Window", on_resize)

# Wait for a key event
cv.waitKey(0)

# Destroy the window
cv.destroyAllWindows()
