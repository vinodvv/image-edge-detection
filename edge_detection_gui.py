import cv2
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt


# Function to perform edge detection
def detect_edges():
    global img, img_display

    # Open file dialog to select an image
    file_path = filedialog.askopenfilename()
    if not file_path:
        return  # If no file is selected, do nothing

    # Load image in grayscale
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error loading image!")
        return

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(img, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred_image, threshold1=100, threshold2=200)

    # Convert the edges image to a format that can be displayed in Tkinter
    img_pil = Image.fromarray(edges)
    img_display = ImageTk.PhotoImage(img_pil)

    # Update the label to show the edge-detected image
    label_image.config(image=img_display)
    label_image.image = img_display

    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
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


# Create the GUI window
window = Tk()
window.title("Edge Detection App")
window.geometry("600x500")

# Label to display the image
label_image = Label(window)
label_image.pack(pady=20)

# Button to load and process the image
btn_load = Button(window, text="Select Image for Edge Detection", command=detect_edges)
btn_load.pack(pady=10)

# Start the GUI event loop
window.mainloop()
