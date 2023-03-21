from coms import Coms
from curses import wrapper
import commands
from joint import Joint

def main(stdscr):
    main_arm = Joint()
    command = commands.move_joint_to_pos(main_arm, 150, 1)
    coms = Coms("/dev/ttyUSB0")
    stdscr.clear()
    stdscr.addstr(0, 0, "Tree Arm v1 i1")

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
