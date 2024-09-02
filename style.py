### LET'S GO.

keras, tf, layers = None
import numpy as np
img_width = 150
img_height = 150

def preprocess_image(image_path): 
   img = keras.utils.load_img(
         image_path, target_size=(img_width, img_height))
   img = keras.utils.img_to_array(img)
   img = np.expand_dims(img, axis=0)
   
   return img

def deprocess_image(img): 
    img = img.reshape((img_height, img_width, 3)) 
    img = np.clip(img, 0, 255).astype("uint8")
    return img

def content_loss(base_img, combination_img):
    return tf.reduce_sum(tf.square(combination_img - base_img))

def gram_matrix(x):
    x = tf.transpose(x, (2, 0, 1))
    features = tf.reshape(x, (tf.shape(x)[0], -1))
    gram = tf.matmul(features, tf.transpose(features))
    return gram

def style_loss(style_img, combination_img):
    S = gram_matrix(style_img)
    C = gram_matrix(combination_img)
    channels = 3
    size = 150 * 150
    return tf.reduce_sum(tf.square(S - C)) / (4.0 * (channels ** 2) * (size ** 2))

def total_variation_loss(x):
    a = tf.square(
            x[:, : img_height - 1, : img_width - 1, :] - x[:, 1:, : img_width - 1, :]
        )
    b = tf.square(
            x[:, : img_height - 1, : img_width - 1, :] - x[:, : img_height - 1, 1:, :]
        )
    return tf.reduce_sum(tf.pow(a + b, 1.25))

class StyleTransfer(keras.Model):
    def __init__(self):
        super().__init__()
        self.preprocess_image = preprocess_image
        self.deprocess_image = deprocess_image
        # Define losses 
        self.content_loss = content_loss
        self.gram_matrix = gram_matrix
        self.style_loss = style_loss
        self.total_variation_loss = total_variation_loss
        self.rescale = layers.Rescaling(1./255)

    
