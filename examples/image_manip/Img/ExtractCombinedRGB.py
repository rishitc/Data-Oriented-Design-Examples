import os
import cv2
import numpy as np
import csv


# IMAGE_PATH = os.path.join("base_image.png")
IMAGE_PATH = os.path.join("base_image.jpeg")

# from PIL import Image

# im = Image.open(IMAGE_PATH) # Can be many different formats.
# pix = im.load()
# print(im.size)  # Get the width and hight of the image for iterating over
# print(pix[x,y])  # Get the RGBA Value of the a pixel of an image
# pix[x,y] = value  # Set the RGBA Value of the image (tuple)
# im.save('alive_parrot.png')  # Save the modified pixels as .png


img = cv2.imread(IMAGE_PATH)

# images are converted to 1:1 dimensions
img = cv2.resize(img, (64, 64)).tolist()
# img = cv2.resize(img, (64, 64))
print(img)
# cv2.imshow("wow", img)
# cv2.waitKey(0)
# for i in img:
#     print(i[0], end=" ")
rgb_csv = open("rgb_csv.csv", "w")
csv_writer = csv.writer(rgb_csv)
csv_writer.writerow([64, 64])

for x in range(64):
    row = []
    for y in range(64):

        # Inserted Rishit's Formula here
        # rgb_combined = img[x][y][2]  # r
        # rgb_combined = (rgb_combined << 8) + img[x][y][1]  # g
        # rgb_combined = (rgb_combined << 8) + img[x][y][0]  # b
        rgb_combined = img[x][y][2] * 65536 + img[x][y][1] * 256 + img[x][y][0]
        # row.append(rgb_combined)
        '''
        # Reversal
        red = (rgb_combined >> 16) & 0xFF;
        green = (rgb_combined >> 8) & 0xFF;
        blue = rgb_combined & 0xFF;
        '''
        # print(rgb_combined, end=", ")
        row.append(rgb_combined)
    csv_writer.writerow(row)

rgb_csv.close()

# print()
