import os
import struct

from datetime import datetime
from functools import wraps


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASCII_FILE = "ascii_spider.txt"


def _get_terminal_size_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            cr = struct.unpack(
                'hh',
                fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'),
            )
            return cr
        except:
            pass
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            return None

    return int(cr[1]), int(cr[0])


def print_center_terminal(string):
    twidth = _get_terminal_size_linux()[0]
    print '\n'.join(
        ('{:^%s}' % twidth).format(s) for s in string.split('\n')
    )


def add_color(color=33):
    def _add_color(func):
        def _decorator(*args, **kwargs):
            print "\033[%sm" % color
            func(*args, **kwargs)
            print "\033[0m"
        return wraps(func)(_decorator)
    return _add_color


@add_color()
def print_ascii_art(filepath):
    with open(filepath, 'r') as filename:
        ascii_art = filename.read()
    print_center_terminal(ascii_art)


@add_color(color=97)
def print_welcome_message():
    welcome_msg = "Welcome my lord, " + \
        os.environ.get("USER") + "... the red spider"
    print_center_terminal(welcome_msg)


@add_color(color=41)
def print_time():
    time = datetime.now()
    welcome_msg = time.strftime('%b %d, %Y')
    print_center_terminal(welcome_msg)


def main():
    print_ascii_art(os.path.join(BASE_DIR, ASCII_FILE))
    print_welcome_message()
    print_time()


if __name__ == "__main__":
    main()
