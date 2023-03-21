from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Tree Arm v1 i1")

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
