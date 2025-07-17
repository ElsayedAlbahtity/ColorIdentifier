import cv2
import pandas as pd

# Load CSV file with color data
colors = pd.read_csv("colors.csv")

# Load and resize image
image = cv2.imread("your_image.jpg")
image = cv2.resize(image, (800, 600))
original_image = image.copy()


# Find closest color name
def get_color_name(b, g, r):
    min_distance = float("inf")
    closest_color = "Unknown"
    for i in range(len(colors)):
        d = abs(int(r) - int(colors.loc[i, "R"])) + \
            abs(int(g) - int(colors.loc[i, "G"])) + \
            abs(int(b) - int(colors.loc[i, "B"]))
        if d < min_distance:
            min_distance = d
            closest_color = colors.loc[i, "color_name"]
    return closest_color

# Variables to store latest click
click_position = None
color_text = ""

def show_color(event, x, y, *_):
    global image, click_position, color_text
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = image[y, x]
        color_name = get_color_name(b, g, r)
        color_text = f"{color_name} (RGB: {r}, {g}, {b})"
        click_position = (x, y)
        image = original_image.copy()

        # Text box size
        (text_width, text_height), _ = cv2.getTextSize(color_text,
                                                       fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                                       fontScale=0.8,
                                                       thickness=2)
        # Draw text background
        box_x, box_y = x + 10, y - 10
        top_left = (box_x - 5, box_y - text_height - 5)
        bottom_right = (box_x + text_width + 5, box_y + 5)
        cv2.rectangle(image, top_left, bottom_right, (255, 255, 255), -1)
        cv2.rectangle(image, top_left, bottom_right, (0, 0, 0), 1)

        # Draw the text
        cv2.putText(image, color_text, (box_x, box_y),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.8,
                    color=(0, 0, 0),
                    thickness=2)

        # Optional: color preview
        cv2.rectangle(image, (box_x - 40, box_y - text_height - 5),
                      (box_x - 10, box_y + 5), (int(b), int(g), int(r)), -1)
        cv2.rectangle(image, (box_x - 40, box_y - text_height - 5),
                      (box_x - 10, box_y + 5), (0, 0, 0), 1)

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", show_color)

while True:
    cv2.imshow("Image", image)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cv2.destroyAllWindows()
