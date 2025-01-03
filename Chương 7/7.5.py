import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

root = tk.Tk()
root.title("Chương trình xem ảnh")

image_path = "otto.jpg"  
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image=photo)
label.pack()

root.mainloop()

root = tk.Tk()
root.title("Chương trình xem ảnh từ URL")

url = "https://example.com/image.png"  
response = requests.get(url)
img = Image.open(BytesIO(response.content))
photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image=photo)
label.pack()

root.mainloop()