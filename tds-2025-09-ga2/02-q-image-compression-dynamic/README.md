# 2. Compress an image (0.75 Marks)

## 1. Problem Description

The task is to download a dynamically generated PNG image and compress it losslessly to a file size under 400 bytes. The compressed image must have the exact same dimensions and pixel data as the original.

## 2. Understanding the Requirements

* **Source Image**: A 500x500 PNG image generated with a specific pattern of red, green, and blue rectangles on a white background.
* **Compression Type**: Lossless. This means no pixel data can be altered.
* **Size Limit**: The final compressed file must be less than 400 bytes.
* **Verification**: The system will check the dimensions and pixel-for-pixel identity against the original image.

## 3. Step-by-Step Solution

1. **Download the Original Image**: In the exam interface, right-click the generated image and "Save Image As...". Let's name it `download.png`.
2. **Inspect the Image**: The original `download.png` will be a simple 500x500 image with a few solid color blocks. Its initial file size will be over 400 bytes (e.g., around 6-7 KB).
3. **Choose a Compression Tool**: A great tool for lossless PNG compression is `Pillow`. Alternatively, you can use an online tool like [Squoosh.app](https://squoosh.app/).
4. **Compress using Squoosh (Easy Method)**:
    * Go to [squoosh.app](https://squoosh.app/).
    * Drag and drop `download.png` into the browser.
    * On the right-hand side, under "Compress", select the **WebP** format.
    * Tick the losessless option.
    * You will see the output file size at the bottom right. Ensure it is below 400 bytes.
    * Click the download button to save the compressed file, naming it `compressed.webp`.

6. **Verify the Result**: Check the file size of `compressed.webp`. It should be under 400 bytes. The dimensions should remain 500x500.
7. **Upload**: Upload the `compressed.webp` file to the exam platform.

## 4. Code / Configuration Files

Alternatively, if you prefer to use a script to automate the compression, here is a simple Python script using the `Pillow` library to convert the PNG to WebP format with lossless compression < 400 bytes:

```python
from PIL import Image
import os


def png_to_webp_lossless(input_path, output_path):
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

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
    print(f"Compressed image saved as {output_file}")
```

Also, you can run this script directly using:

```bash
uv run https://raw.githubusercontent.com/mynkpdr/tds-sep-2025/refs/heads/main/tds-2025-09-ga2/02-q-image-compression-dynamic/compress.py
```

## 5. How to Verify

The final verification happens on the exam platform. It will check:

1. That the uploaded file is a valid image.
2. That its size is less than 400 bytes.
3. That its dimensions are 500x500.
4. That every pixel is identical to the original generated image.

If you followed the lossless compression steps correctly, the verification will pass.
