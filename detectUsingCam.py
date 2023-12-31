import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import cv2

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
model = tf.keras.models.load_model('keras_model.h5')



# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
    
shape = (1, 224, 224, 3)
data  = np.ndarray(shape, dtype=np.float32)
vid = cv2.VideoCapture(1)

while 1:
    r, frame = vid.read()
    cv2.imwrite('E:\GitLearn\ProjectUsingNumpy\camFrame' + ".jpg", frame)


    # Replace this with the path to your image
    image_name = 'camFrame.jpg'
    image = Image.open(image_name)
    
    # Load the labels
    with open('labels.txt', 'r') as f:
        class_name = f.read().split('\n')

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    #image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)

    if(np.max(prediction) < 0.7):
        
        image = cv2.imread(image_name)
        height, width, process = image.shape
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, "none", (20, 30), font, 1, (0, 255, 0), 1, cv2.LINE_AA)
    else:
        index = np.argmax(prediction) 
        class_name = class_name[index]
        index = np.argmax(prediction)
        #print(index)

        print("Class Name : ", class_name)
        image = cv2.imread(image_name)
        height, width, process = image.shape
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, class_name, (20, 30), font, 1, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow("Image", image)
    k = cv2.waitKey(30) & 0xff
    if k == ord("q"):
        break
    
vid.release()
cv2.destroyAllWindows()
    
    

