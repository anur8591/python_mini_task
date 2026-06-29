from itertools import cycle
from PIL import Image, ImageTk
import time 
import tkinter as tk

root=tk.Tk()
root.title("Image slideshow viewer")

# list of image path
image_paths = [
    r"C:\Users\Anurag\OneDrive\Desktop\python_mini_task\image\61RSL9s1J8L._AC_UF894,1000_QL80_.jpg",
    r"C:\Users\Anurag\OneDrive\Desktop\python_mini_task\image\BMW-M4-GT41-1220x661.jpeg",
    r"C:\Users\Anurag\OneDrive\Desktop\python_mini_task\image\bmw-m4-meet-beast.jpg",
    r"C:\Users\Anurag\OneDrive\Desktop\python_mini_task\image\G90-BMW-M5-CS-01.jpg",
    r"C:\Users\Anurag\OneDrive\Desktop\python_mini_task\image\hq720.jpg",
    r"C:\Users\Anurag\OneDrive\Desktop\python_mini_task\image\images (1).jpg",
    r"C:\Users\Anurag\OneDrive\Desktop\python_mini_task\image\images (2).jpg",
    r"C:\Users\Anurag\OneDrive\Desktop\python_mini_task\image\images.jpg",
    r"C:\Users\Anurag\OneDrive\Desktop\python_mini_task\image\P90411344-the-new-bmw-m5-cs-studio-01-2021-600px.jpg",
    r"C:\Users\Anurag\OneDrive\Desktop\python_mini_task\image\P90468919_highRes_munich-ger-17-june-2.jpg",
]
#resize the image to 1080x1080
image_size=(1080,1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
# converting into photoimageobject to use in tkinter 
photo_images = [ImageTk.PhotoImage(image) for image in images]

