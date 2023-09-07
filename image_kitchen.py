from PIL import Image
import os
import sys

class ImageProcessor:
    def __init__(self):
        pass

    def convert_to_png(self, image_path, output_path):
        """
        Converts all the .jpg images in the specified `image_path` directory to .png format and saves them in the `output_path` directory.

        Parameters:
            image_path (str): The path to the directory containing the .jpg images.
            output_path (str): The path to the directory where the converted .png images will be saved.

        Returns:
            None
        
            prints:
            A message for each image converted to PNG format
        """
        for filename in os.listdir(image_path):
            if filename.endswith('.jpg', '.jpeg'):
                img = Image.open(os.path.join(image_path, filename))
                clean_name = os.path.splitext(filename)[0]
                img.save(os.path.join(output_path, f'{clean_name}.png'), 'png')
                print(f'{filename} converted to png')

    def convert_to_jpg(self, image_path, output_path):
        """
        Converts all PNG images in a given directory to JPG format.

        Args:
            image_path (str): The path to the directory containing PNG images.
            output_path (str): The path to the directory where the converted JPG images will be saved.

        Returns:
            None

        Prints:
            A message for each image converted to JPG format.
        """
        for filename in os.listdir(image_path):
            if filename.endswith('.png'):
                img = Image.open(os.path.join(image_path, filename))
                clean_name = os.path.splitext(filename)[0]
                img.save(os.path.join(output_path, f'{clean_name}.jpg'), 'jpg')
                print(f'{filename} converted to jpg')

    def crop_image(self, image_path, output_path, left, top, right, bottom):
        """
        Crop the images in the specified directory.

        Parameters:
            image_path (str): The path to the directory containing the images.
            output_path (str): The path to the directory where the cropped images will be saved.
            left (int): The left coordinate of the cropping box.
            top (int): The top coordinate of the cropping box.
            right (int): The right coordinate of the cropping box.
            bottom (int): The bottom coordinate of the cropping box.

        Returns:
            None

        Prints:
            A message for each image cropped
        """
        for filename in os.listdir(image_path):
            if filename.endswith(('.jpg','.jpeg', '.png')):
                img = Image.open(os.path.join(image_path, filename))
                box = (left, top, right, bottom)
                region = img.crop(box)
                region.save(os.path.join(output_path, filename))
                print(f'{filename} cropped')

    def resize_image(self, image_path, output_path, width, height):
        """
        Resizes images in a given directory to a specified width and height.

        Args:
            image_path (str): The path to the directory containing the images to be resized.
            output_path (str): The path to the directory where the resized images will be saved.
            width (int): The desired width of the resized images.
            height (int): The desired height of the resized images.

        Returns:
            None
        
        prints:
            A message for each image resized
        """
        for filename in os.listdir(image_path):
            if filename.endswith(('.jpg','.jpeg', '.png')):
                img = Image.open(os.path.join(image_path, filename))
                img = img.resize((width, height))
                img.save(os.path.join(output_path, filename))
                print(f'{filename} resized')

    def image_thumbnail(self, image_path, output_path, width, height):
        """
        Generate a thumbnail for each image in the specified directory.

        Args:
            image_path (str): The path to the directory containing the images.
            output_path (str): The path to the directory where the thumbnails will be saved.
            width (int): The desired width of the thumbnail.
            height (int): The desired height of the thumbnail.

        Returns:
            None

        Prints:
            A message for each thumbnail generated.
        """
        for filename in os.listdir(image_path):
            if filename.endswith(('.jpg','.jpeg', '.png')):
                img = Image.open(os.path.join(image_path, filename))
                box = (width, height)
                img.thumbnail(box)
                img.save(os.path.join(output_path, filename))
                print(f'{filename} thumbnail')

def main():
    processor = ImageProcessor()

    try:
        while True:
            print("Enter 1 to convert JPG to PNG")
            print("Enter 2 to convert PNG to JPG")
            print("Enter 3 to crop image")
            print("Enter 4 to resize image")
            print("Enter 5 to thumbnail image")
            print("Enter 6 to exit")

            user_input = int(input("Enter your choice 1-6: "))

            if user_input == 1:
                image_path = input("Enter image path: ")
                output_path = input("Enter output path: ")
                processor.convert_to_png(image_path, output_path)
            
            elif user_input == 2:
                image_path = input("Enter image path: ")
                output_path = input("Enter output path: ")
                processor.convert_to_jpg(image_path, output_path)
            
            elif user_input == 3:
                image_path = input("Enter image path: ")
                output_path = input("Enter output path: ")
                left = int(input("Enter left coordinate: "))
                top = int(input("Enter top coordinate: "))
                right = int(input("Enter right coordinate: "))
                bottom = int(input("Enter bottom coordinate: "))
                processor.crop_image(image_path, output_path, left, top, right, bottom)
            
            elif user_input == 4:
                image_path = input("Enter image path: ")
                output_path = input("Enter output path: ")
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                processor.resize_image(image_path, output_path, width, height)

            elif user_input == 5:
                image_path = input("Enter image path: ")
                output_path = input("Enter output path: ")
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                processor.image_thumbnail(image_path, output_path, width, height)
            elif user_input == 6:
                break
            else:
                print("Invalid choice. Please select 1-6.")
    except FileNotFoundError as err:
        print('File not found:', err)

if __name__ == '__main__':
    main()
