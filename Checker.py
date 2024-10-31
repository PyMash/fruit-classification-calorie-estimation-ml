
from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.initializers import GlorotNormal
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
# Dictionary mapping fruit names to average calories per 100 grams
fruit_calories_per_100g = {
    'Apple': 52,
    'Banana': 89,
    'Cherry': 50,
    'Chickoo': 94,
    'Grapes': 69,
    'Kiwi': 61,
    'Mango': 60,
    'Orange': 47,
    'Strawberry': 32
}



# Function to calculate the default size of the GUI window
def calculate_window_size(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = int(0.35 * screen_width)
    window_height = int(0.4 * screen_height)
    return f"{window_width}x{window_height}"

# Load the trained model
model = tf.keras.models.load_model('kaggle/working/myFruitclassifier001')

# Dictionary mapping class indices to class labels
class_labels = {0: 'Apple', 1: 'Banana', 2: 'Cherry', 3: 'Chickoo', 4: 'Grapes', 5: 'Kiwi', 6: 'Mango', 7: 'Orange', 8: 'Strawberry'}

def select_image():
    file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        image_label.configure(image=img)
        image_label.image = img
        predict_fruit(file_path)

def predict_fruit(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Rescale to [0, 1]

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class_label = class_labels.get(predicted_class_index, "Unknown")
    accuracy = predictions[0][predicted_class_index] * 100

    if accuracy < 97:
        predicted_class_label = "Unknown"
        result_text.set(f"Predicted Fruit: {predicted_class_label}")
    else:
        predicted_class_label = class_labels.get(predicted_class_index, "Unknown")
        predicted_calories_per_100g = fruit_calories_per_100g.get(predicted_class_label, "Unknown")
        result_text.set(f"Predicted Fruit: {predicted_class_label}\nAccuracy: {accuracy:.2f}%\nAverage Calories per 100g: {predicted_calories_per_100g}")

    

root = tk.Tk()
root.title("Fruit Classifier")

# Calculate the default window size based on screen size
default_window_size = calculate_window_size(root)
root.geometry(default_window_size)

# Create a frame to contain the button
button_frame = tk.Frame(root)
button_frame.pack(expand=True)  # Expand to fill the window

select_button = tk.Button(button_frame, text="Select Image", command=select_image)
select_button.pack(pady=10, padx=10, anchor="center")  # Center the button

image_label = tk.Label(root)
image_label.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack(pady=10)

root.mainloop()

