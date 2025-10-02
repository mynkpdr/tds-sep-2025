import os


def rename_files_in_directory(directory="."):
    """
    Renames files in the specified directory according to the digit-swapping rule.
    (0->1, 1->2, ..., 9->0)
    """
    try:
        filenames = [
            f
            for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        ]
        print(f"Found {len(filenames)} files to process...")

        for old_name in filenames:
            if old_name == "rename.py":
                continue  # Don't rename the script itself

            new_name = ""
            for char in old_name:
                if char.isdigit():
                    new_digit = (int(char) + 1) % 10
                    new_name += str(new_digit)
                else:
                    new_name += char

            if old_name != new_name:
                old_path = os.path.join(directory, old_name)
                new_path = os.path.join(directory, new_name)
                os.rename(old_path, new_path)
                print(f'Renamed "{old_name}" to "{new_name}"')

        print("Renaming complete.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    rename_files_in_directory()
