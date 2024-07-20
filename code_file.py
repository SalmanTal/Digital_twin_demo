import cv2
import numpy as np
import random

def process_frame(frame):
    # Preprocessing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Contour detection
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Filter and approximate polygon
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) > 4:  # Assuming the goods carriage vehicle has more than 4 vertices
            polygon = approx
            break

    # Grid creation
    x, y, w, h = cv2.boundingRect(polygon)
    grid_points = [(i, j) for i in range(x, x+w) for j in range(y, y+h)]

    # Random point selection
    random_point = random.choice(grid_points)
    print("random point cordinate",random_point)
    # Coordinate conversion
    center_x, center_y = x + w//2, y + h//2
    dx, dy = random_point[0] - center_x, random_point[1] - center_y
    r = np.sqrt(dx*2 + dy*2)
    theta = np.arctan2(dy, dx)
    print("R",r)
    print("theta ", theta)


    # Display results
    cv2.drawContours(frame, [polygon], -1, (0, 255, 0), 2)
    cv2.circle(frame, random_point, 5, (255, 0, 0), -1)
    cv2.imshow('Frame', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return r,theta,random_point

# Function to use camera
def use_camera():
    # Initialize the camera
    camera = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture an image from the camera
    ret, frame = camera.read()

    # Check if frame is captured successfully
    if not ret:
        print("Error: Could not read frame.")
    else:
        process_frame(frame)

    # Release the camera
    camera.release()

# Function to use a saved image
def use_saved_image(image_path):
    frame = cv2.imread(image_path)
    if frame is None:
        print("Error: Could not read the image.")
    else:
        process_frame(frame)

# Uncomment the line below to use the camera
# use_camera()

# Uncomment the line below to use a saved image (provide the correct path)
path1=r"F:\Salman codes\Open_CV_Course\Edge_Detection\final_wagon_image2.png"
use_saved_image(path1)
# print(f'value of R{r}, theta {theta}, random_point {random_point}')