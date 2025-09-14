import os
from PIL import Image

def resize_images_in_directory():
    """
    This function resizes all images in the current directory to 500x500 pixels.
    It overwrites the original files.
    """
    # Define the target resolution
    target_size = (320, 320)
    
    # Get the current directory
    current_directory = os.getcwd()
    print(f"Scanning for images in: {current_directory}...")

    # List of common image file extensions
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')

    # Loop through all files in the directory
    for filename in os.listdir(current_directory):
        # Check if the file is an image
        if filename.lower().endswith(image_extensions):
            filepath = os.path.join(current_directory, filename)
            try:
                # Open the image file
                with Image.open(filepath) as img:
                    print(f"Resizing '{filename}'...")
                    
                    # Resize the image. Image.Resampling.LANCZOS provides high-quality downscaling.
                    resized_img = img.resize(target_size, Image.Resampling.LANCZOS)
                    
                    # Save the resized image, overwriting the original
                    resized_img.save(filepath)
                    
                    print(f"✅ Successfully resized '{filename}' to {target_size[0]}x{target_size[1]}")

            except Exception as e:
                print(f"❌ Could not process '{filename}'. Reason: {e}")

    print("\nImage resizing complete! ✨")

if __name__ == '__main__':
    resize_images_in_directory()