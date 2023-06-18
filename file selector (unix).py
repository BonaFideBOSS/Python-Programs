import os
import curses

def get_file_selection(stdscr, files):
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr("Select a file:\n")
        for i, file in enumerate(files):
            if i == current_row:
                stdscr.addstr(f"-> {file}\n")
            else:
                stdscr.addstr(f"   {file}\n")

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(files) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return files[current_row]

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    # Get list of .txt and .csv files in current directory
    files = [file for file in os.listdir() if file.endswith(('.txt', '.csv'))]

    # Select a file
    selected_file = get_file_selection(stdscr, files)
    stdscr.addstr(f"\nYou selected: {selected_file}")
    stdscr.getch()

curses.wrapper(main)
