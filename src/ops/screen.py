import src
import logging
import pyautogui as cursor


logger = logging.getLogger(__name__)

width, height = cursor.size()
logger.info(f"Screen size '{height} x {width}'")


ORIGIN = (0.17, 0.145)
N = 17
M = 11


dx = 0.074
dy = 0.02585


def debug():
    """
    Dev method
    """
    x, y = ORIGIN
    dx = 0.074
    cursor.moveTo(int((x)*width), int(y*height), duration=1)

    dy = 0.02585
    for i in range(1, N+1):
        cursor.moveTo(int((x)*width), int((y+i*dy)*height), duration=0.25)


def label_selection(p: int) -> None:
    """
    Selects a label in the grid position `p` in a  grid with `t` total items

    * calculates cell location of item index `p`
    * moves and clicks in the location
    * returns to original position
    """
    x, y = ORIGIN
    position = cursor.position()

    n = p // M
    m = p % M
    logger.info(f"Moving to cell '({n},{m})'")

    px = (x + m*dx) * width
    py = (y + n*dy) * height

    cursor.doubleClick(px, py)
    cursor.moveTo(*position)

