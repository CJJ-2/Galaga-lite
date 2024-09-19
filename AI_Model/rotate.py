from PIL import Image
import os

def rotate_images(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Loop through each file in the folder
    for file_name in files:
        # Check if the file is an image (you can extend this check as needed)
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Construct the full file path
            file_path = os.path.join(folder_path, file_name)

            # Open the image
            image = Image.open(file_path)

            # Rotate the image by 90 degrees
            rotated_image = image.rotate(90)

            # Save the rotated image (you may overwrite the original or save to a new folder)
            rotated_image.save(os.path.join(folder_path, f"rotated_{file_name}"))

            print(f"Rotated: {file_name}")

if __name__ == "__main__":
    # Specify the path to your image folder
    image_folder_path = "image_data/Stop"

    # Call the function to rotate images in the specified folder
    rotate_images(image_folder_path)
