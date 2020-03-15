import abc


class Widget(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass


class TextField(Widget):
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def draw(self):
        print("Textfield: {}, {}".format(self._width, self._height))


class Decorator(Widget):
    def __init__(self, widget: Widget):
        self._widget = widget

    def draw(self):
        self._widget.draw()


class BorderDecorator(Decorator):
    def __init__(self, widget: Widget):
        super().__init__(widget)

    def draw(self):
        print("--------------------")
        super().draw()


class DoubleBorderDecorator(Decorator):
    def __init__(self, widget: Widget):
        super().__init__(widget)

    def draw(self):
        print("====================")
        super().draw()


def main():
    widget = DoubleBorderDecorator(BorderDecorator(TextField(100, 200)))
    widget.draw()


if __name__ == "__main__":
    main()

