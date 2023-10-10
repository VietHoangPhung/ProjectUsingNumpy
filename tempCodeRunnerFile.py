model = tf.keras.models.load_model('keras_model.h5')

# Load the labels
with open('labels.txt', 'r') as f:
    class_name = f.read().split('\n')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.