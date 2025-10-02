def compare_files(file1_path="a.txt", file2_path="b.txt"):
    """
    Compares two files line by line and counts the number of differing lines.
    """
    try:
        with open(file1_path, "r", encoding="utf-8") as f1, open(
            file2_path, "r", encoding="utf-8"
        ) as f2:

            lines1 = f1.readlines()
            lines2 = f2.readlines()

            diff_count = 0
            max_lines = max(len(lines1), len(lines2))

            for i in range(max_lines):
                line1 = lines1[i].strip() if i < len(lines1) else ""
                line2 = lines2[i].strip() if i < len(lines2) else ""

                if line1 != line2:
                    diff_count += 1

            print(f"Number of different lines: {diff_count}")
            return diff_count

    except FileNotFoundError:
        print(
            "Error: Make sure both a.txt and b.txt are in the same directory as this script."
        )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    compare_files()
