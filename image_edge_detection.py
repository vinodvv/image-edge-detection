import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = "images/image_3.jpeg"  # Provide your image path here
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image loaded successfully
if image is None:
    print("Error loading image!")
    exit()

# Apply Gaussian Blur to reduce noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Canny Edge Detection
edges = cv2.Canny(blurred_image, threshold1=100, threshold2=200)

# Original image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Edge-detected image
plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detected Image")
plt.axis('off')

# Show the plot
plt.show()

# Optionally save the edge-detected image
cv2.imwrite('output/edges_detected.jpg', edges)
