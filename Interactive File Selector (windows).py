import os
import msvcrt

def get_file_selection(files):
    current_row = 0

    while True:
        os.system('cls')
        print("Select a file:")
        for i, file in enumerate(files):
            if i == current_row:
                print(f"-> {file}")
            else:
                print(f"   {file}")

        key = msvcrt.getch()

        if key == b'\xe0':  # arrow key prefix
            key = msvcrt.getch()
            if key == b'H' and current_row > 0:  # up arrow
                current_row -= 1
            elif key == b'P' and current_row < len(files) - 1:  # down arrow
                current_row += 1
        elif key == b'\r':  # Enter key
            return files[current_row]

def main():
    # Get list of .txt and .csv files in current directory
    files = [file for file in os.listdir()]
    # Filtered
    #files = [file for file in os.listdir() if file.endswith(('.txt', '.csv'))]

    # Select a file
    selected_file = get_file_selection(files)
    print("\nYou selected:", selected_file)
    input("Press Enter to exit...")


main()
