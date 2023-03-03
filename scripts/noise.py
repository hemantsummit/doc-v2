import cv2
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import os
from PIL import Image
import PIL
import numpy as np
from skimage.util import random_noise
import random

def horizontal_shift(folder_path):
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

    for filename in file_list:
        load_img = cv2.imread(os.path.join(folder_path, filename))
        img = tf.expand_dims(load_img, 0)

        # create image data augmentation with horizontal shifting
        datagen = ImageDataGenerator(width_shift_range=[-10,10])

        it = datagen.flow(img, batch_size=1)
        
        batch = it.next()
        batch = it.next()
        batch = it.next()

        shifted_filename = os.path.join(folder_path, filename)
        cv2.imwrite(shifted_filename, batch[0])

def vertical_shift(folder_path):
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

    for filename in file_list:
        load_img = cv2.imread(os.path.join(folder_path, filename))
        img = tf.expand_dims(load_img, 0)

        datagen = ImageDataGenerator(height_shift_range=0.5)

        it = datagen.flow(img, batch_size=1)
        
        batch = it.next()
        batch = it.next()
        batch = it.next()

        shifted_filename = os.path.join(folder_path, filename)
        cv2.imwrite(shifted_filename, batch[0])

def rotation(folder_path):
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

    for filename in file_list:
        load_img = cv2.imread(os.path.join(folder_path, filename))
        img = tf.expand_dims(load_img, 0)

        # create image data augmentation with rotation range 0-10 degrees
        datagen = ImageDataGenerator(rotation_range=3)

        it = datagen.flow(img, batch_size=1)
        
        batch = it.next()
        batch = it.next()
        batch = it.next()

        shifted_filename = os.path.join(folder_path, filename)
        cv2.imwrite(shifted_filename, batch[0])

def zoom(folder_path):
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

    for filename in file_list:
        load_img = cv2.imread(os.path.join(folder_path, filename))
        img = tf.expand_dims(load_img, 0)

        datagen = ImageDataGenerator(zoom_range=[0.5,1])

        it = datagen.flow(img, batch_size=1)
        
        batch = it.next()
        batch = it.next()
        batch = it.next()

        shifted_filename = os.path.join(folder_path, filename)
        cv2.imwrite(shifted_filename, batch[0])

def brightness(folder_path):
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

    for filename in file_list:
        load_img = cv2.imread(os.path.join(folder_path, filename))
        img = tf.expand_dims(load_img, 0)

        datagen = ImageDataGenerator(brightness_range=[0.1,0.5])

        it = datagen.flow(img, batch_size=1)
        
        batch = it.next()
        batch = it.next()
        batch = it.next()

        shifted_filename = os.path.join(folder_path, filename)
        cv2.imwrite(shifted_filename, batch[0])

def noise(folder_path):
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

    for filename in file_list:
        load_img = cv2.imread(os.path.join(folder_path, filename))
        img = tf.expand_dims(load_img, 0)

        # Noise
        noise = random_noise(load_img, mode='s&p', amount=0.05)
        noise = np.array(255*noise, dtype = 'uint8')

        shifted_filename = os.path.join(folder_path, filename)
        cv2.imwrite(shifted_filename, noise)

def scaling(folder_path):
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

    for filename in file_list:
        load_img = Image.open(os.path.join(folder_path, filename))

        resized_image = load_img.resize((500+random.randint(0,100),800+random.randint(0,100)))

        resized_image.save(os.path.join(folder_path, filename))

def saturation(folder_path):
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

    for filename in file_list:
        load_img = Image.open(os.path.join(folder_path, filename))

        converter = PIL.ImageEnhance.Color(load_img)
        resized_image = converter.enhance(random.randint(1,4)/7.0)

        resized_image.save(os.path.join(folder_path, filename))

# folder_path_format -> C:/Users/HYadav/Desktop/Folder

brightness("./before")