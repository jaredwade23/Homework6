from graphics import GraphWin, Point, Rectangle, Text


def clicked(point):
    if 150 <= point.getX() <= 250 and 120 <= point.getY() <= 180:
        return True
    else:
        return False


def main():
    win = GraphWin("Button Test", 400, 300)

    button = Rectangle(Point(150, 120), Point(250, 180))
    button.draw(win)

    label = Text(Point(200, 150), "BUTTON")
    label.draw(win)

    for i in range(10):
        point = win.getMouse()

        if clicked(point):
            print("Button was clicked.")
        else:
            print("Button was not clicked.")

    win.close()


main()