from PIL import Image
import os

def png_to_webp_lossless(input_path, output_path):
    img = Image.open(input_path)

    # Save as WebP lossless
    img.save(output_path, "WEBP", lossless=True, quality=100)

    original_size = os.path.getsize(input_path)
    webp_size = os.path.getsize(output_path)

    print(f"Original PNG size: {original_size} bytes")
    print(f"WebP (lossless) size: {webp_size} bytes")

if __name__ == "__main__":
    input_file = "download.png"
    output_file = "download_lossless.webp"
    png_to_webp_lossless(input_file, output_file)
