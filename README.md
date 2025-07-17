# 🎨 ColorIdentifier

A beginner-friendly Python project that identifies the name of the color when you click on any part of an image.

## 📂 Project Structure

- `color_identifier.py`: Main script to run the app.
- `colors.csv`: Dataset containing color names and RGB values.
- `your_image.jpg`: Sample image to try the project.
- `README.md`: This file.

## 🚀 How to Run

1. Clone the repo or download it:
   ```bash
   git clone https://github.com/ElsayedAlbahlity/ColorIdentifier.git

2. Install required libraries:
   ```bash
   pip install opencv-python pandas


python color_identifier.py


Then click anywhere on the image, and the app will tell you the color name 🎯

## 🧠 How it Works

- The script opens an image using OpenCV.
- When the user clicks on a point, it reads the color at that pixel.
- It compares the RGB value with a color database from `colors.csv`.
- It shows the closest color name on the image in real-time.

## 📸 Screenshot

![sample](your_image.jpg)

## 🧑‍💻 Author

Made by [Elsayed Albahtity](https://github.com/ElsayedAlbahtity) during the **UneeQ Interns** challenge ✨
