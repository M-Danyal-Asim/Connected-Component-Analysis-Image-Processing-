import numpy as np
import cv2 as cv
image_1 = cv.imread('Picture6.png', 0)
print(image_1)
dimensions = np.shape(image_1)
width = image_1.shape[0]
height = image_1.shape[1];
image_2 = np.zeros(dimensions, dtype=np.uint16)
# thresholding our image to get it into the binary
for row in range(0, width):
    for col in range(0, height):
        if image_1[row][col] >= 127:
            image_1[row][col] = 1
        else:
            image_1[row][col] = 0
print(image_1)
cv.imwrite('Picture.png', image_1)
equivalency_list = [0]
Label = 0
for row in range(0, dimensions[0]):
    for col in range(0, dimensions[1]):
        if image_1[row, col] == 1:
            top_value = image_2[row - 1, col]
            backward_value = image_2[row, col - 1]
            if top_value == 0 and backward_value == 0:
                Label = Label + 1
                equivalency_list.append(Label)
                image_2[row, col] = Label
            elif top_value == 0 and backward_value != 0:
                 image_2[row, col] = backward_value
            elif top_value != 0 and backward_value == 0:
                image_2[row, col] = top_value
            elif top_value == backward_value:
                image_2[row, col] = top_value
            else:
                a = min(equivalency_list[top_value], equivalency_list[backward_value])
                b = max(equivalency_list[top_value], equivalency_list[backward_value])
                c = equivalency_list[b]
                image_2[row, col] = a
                for p in range(np.shape(equivalency_list)[0]):
                    if equivalency_list[p] == b:
                        equivalency_list[p] = a
print("No of Objects in image are:", np.count_nonzero(np.unique(equivalency_list)))
