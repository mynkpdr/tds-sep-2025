# 12. Reconstruct an image (1 Mark)

## 1. Problem Description

The task is to write a Python script to reconstruct a scrambled image for **PixelGuard Solutions**, a digital forensics firm. The original image was cut into a 5x5 grid (25 pieces) and rearranged.

You are given the scrambled image and a "mapping file" (in the form of a table) that specifies where each piece *should* go. Your goal is to use a Python script with the **Pillow** library to "un-scramble" the image and save the result.

## 2. Understanding the Requirements

  - **Language**: Python.
  - **Library**: `Pillow` (PIL).
  - **Input**:
    1.  A scrambled image file (`jigsaw.webp`).
    2.  A mapping of `(Original Row, Original Column)` to `(Scrambled Row, Scrambled Column)`.
  - **Logic**:
    1.  **Load the Map**: The map from the question tells you, for example, "The piece at scrambled (0,0) *belongs* at original (2,1)".
    2.  **Inverse Map**: You need to *inverse* this logic. Your script needs to ask: "For the top-left (0,0) spot in my *new* image, which piece do I get from the *scrambled* image?"
          - *Example*: The question table shows `Original (0,0)` maps to `Scrambled (2,0)`.
          - This means: To fill `(0,0)` of your *new* image, you must grab the piece from `(2,0)` of the *scrambled* image.
    3.  **Create New Image**: Create a new, blank image of the same size (e.g., 500x500).
    4.  **Calculate Piece Size**: The image is 5x5, so if it's 500x500, each piece is 100x100.
    5.  **Loop and Paste**:
          - Iterate through all 25 *original* positions (e.g., `orig_row` from 0 to 4, `orig_col` from 0 to 4).
          - For each position, find its corresponding `(scrambled_row, scrambled_col)` from the map.
          - **Crop** the piece from the `scrambled` image at the `(scrambled_row, scrambled_col)` location.
          - **Paste** that piece into the `new` image at the `(orig_row, orig_col)` location.
    6.  **Save Image**: Save the final, reconstructed image.
  - **Output**: The reconstructed image file, which you must upload.

## 3. Step-by-Step Solution

### Step 1: Set Up Environment

1.  Create a project folder (e.g., `image_reconstruct`).
2.  Create and activate a virtual environment.
3.  Install `Pillow`: `pip install Pillow`.
4.  Create a Python file (e.g., `reconstruct.py`).
5.  Download the `jigsaw.webp` file into the same folder.

### Step 2: Write the Python Script

1.  **Import**: `from PIL import Image`.
2.  **Define Map**: Hard-code the mapping from the question into a Python dictionary. It's *easier* to code the *inverse map* directly: `(orig_r, orig_c): (scrambled_r, scrambled_c)`.
3.  **Load Image**: `img = Image.open("jigsaw.webp")`.
4.  **Get Dimensions**: `width, height = img.size`. `piece_width = width // 5`.
5.  **Create New Image**: `new_img = Image.new("RGB", (width, height))`.
6.  **Loop**: Use a nested `for` loop, `for r in range(5): for c in range(5):`.
7.  **Get Scrambled Coords**: Look up `(r, c)` in your inverse map to find `(scrambled_r, scrambled_c)`.
8.  **Define Crop Box**: Calculate the pixel coordinates for the scrambled piece:
      - `left = scrambled_c * piece_width`
      - `top = scrambled_r * piece_height`
      - `box = (left, top, left + piece_width, top + piece_height)`
9.  **Crop**: `piece = img.crop(box)`.
10. **Define Paste Position**: Calculate where to paste on the *new* image:
      - `paste_x = c * piece_width`
      - `paste_y = r * piece_height`
11. **Paste**: `new_img.paste(piece, (paste_x, paste_y))`.
12. **Save**: `new_img.save("reconstructed.png")`.

## 4. Code (`reconstruct.py`)

```python
from PIL import Image
import os

def reconstruct_image(scrambled_file, output_file):
    """
    Reconstructs a 5x5 scrambled image using the provided map.
    """
    
    # This is the map from the question, formatted as:
    # (Scrambled Row, Scrambled Col): (Original Row, Original Col)
    # We invert it to:
    # (Original Row, Original Col): (Scrambled Row, Scrambled Col)
    
    # Original (0,0) <- Scrambled (2,0)
    # Original (0,1) <- Scrambled (0,4)
    # ...
    
    inverse_map = {
        (0,0): (2,0), (0,1): (0,4), (0,2): (3,4), (0,3): (0,3), (0,4): (4,3),
        (1,0): (3,0), (1,1): (0,1), (1,2): (4,1), (1,3): (4,2), (1,4): (1,0),
        (2,0): (1,1), (2,1): (0,0), (2,2): (1,4), (2,3): (3,1), (2,4): (1,2),
        (3,0): (2,3), (3,1): (4,0), (3,2): (2,1), (3,3): (3,2), (3,4): (2,4),
        (4,0): (4,4), (4,1): (0,2), (4,2): (1,3), (4,3): (2,2), (4,4): (3,3)
    }
    
    print(f"Loading scrambled image: {scrambled_file}")
    try:
        img = Image.open(scrambled_file)
    except FileNotFoundError:
        print(f"Error: File not found. Make sure '{scrambled_file}' is in the same directory.")
        return

    width, height = img.size
    if width != 500 or height != 500:
        print(f"Warning: Image is not 500x500. Assuming 5x5 grid.")

    piece_width = width // 5
    piece_height = height // 5
    
    print(f"Image size: {width}x{height}. Piece size: {piece_width}x{piece_height}")

    # Create a new blank image
    new_img = Image.new("RGB", (width, height))
    
    # Loop through all 25 *original* positions
    for orig_r in range(5):
        for orig_c in range(5):
            
            # 1. Find which scrambled piece belongs here
            scrambled_r, scrambled_c = inverse_map[(orig_r, orig_c)]
            
            # 2. Define the crop box for the scrambled image
            scrambled_x = scrambled_c * piece_width
            scrambled_y = scrambled_r * piece_height
            crop_box = (scrambled_x, scrambled_y, scrambled_x + piece_width, scrambled_y + piece_height)
            
            # 3. Crop the piece
            piece = img.crop(crop_box)
            
            # 4. Define the paste position for the new image
            paste_x = orig_c * piece_width
            paste_y = orig_r * piece_height
            
            # 5. Paste the piece
            new_img.paste(piece, (paste_x, paste_y))

    # Save the final image
    new_img.save(output_file)
    print(f"\n--- Result ---")
    print(f"Successfully saved reconstructed image to: {output_file}")
    print("----------------\n")


if __name__ == "__main__":
    INPUT_IMAGE = "jigsaw.webp"
    OUTPUT_IMAGE = "reconstructed.png" # Save as PNG for lossless quality
    
    reconstruct_image(INPUT_IMAGE, OUTPUT_IMAGE)

```

## 5. How to Run

1.  Install Pillow: `pip install Pillow`.
2.  Save the code as `reconstruct.py`.
3.  Download `jigsaw.webp` to the same directory.
4.  Run the script from your terminal:
    ```bash
    python reconstruct.py
    ```
5.  The script will create a new file named `reconstructed.png`.
6.  **This `reconstructed.png` file is your answer.** You must upload this file to the answer box.