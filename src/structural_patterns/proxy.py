class GumballMachine:
    def __init__(self, location: str, count: int):
        self._location = location
        self._count = count
        self._state = ""

    def location(self) -> str:
        return self._location

    def count(self) -> int:
        return self._count

    def state(self) -> str:
        return self._state


class GumballProxy:
    def __init__(self, gumball_machine: GumballMachine):
        self._gumball_machine = gumball_machine

    def report(self) -> None:
        print("Gumball Machine {}".format(self._gumball_machine.location()))
        print("Current inventory {}".format(self._gumball_machine.count()))
        print("Current state {}".format(self._gumball_machine.state()))


def main():
    count = 0
    gumball_machine = GumballMachine("Madrid", 6)
    proxy = GumballProxy(gumball_machine)

    proxy.report()


if __name__ == "__main__":
    main()

