import abc


class AmericanPlug(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def plug(self):
        print("Plugging european plug")


class EuropeanPlug:
    def plug(self):
        print("Plugging european plug")


class AmericanSocket:
    def connect(self, plug: AmericanPlug):
        if not isinstance(plug, AmericanPlug):
            exit("Wrong plug connected")

        plug.plug()
        print("American plug connected")


class EuropeanToAmericanPlugAdapter(AmericanPlug):
    def __init__(self, european_plug: EuropeanPlug):
        self._european_plug = european_plug

    def plug(self):
        # do something here
        self._european_plug.plug()


def main():
    socket = AmericanSocket()
    euro_plug = EuropeanPlug()
    socket.connect(EuropeanToAmericanPlugAdapter(euro_plug))


if __name__ == "__main__":
    main()
