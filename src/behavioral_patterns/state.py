import abc


class Chain:
    def __init__(self):
        self._current = Off()

    def set_state(self, state):
        self._current = state

    def pull(self):
        self._current.pull(self)


class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pull(self, wrapper: Chain):
        wrapper.set_state(Off())
        print("turning off")


class Off(State):
    def pull(self, wrapper: Chain):
        wrapper.set_state(Low())
        print("low speed")


class Low(State):
    def pull(self, wrapper: Chain):
        wrapper.set_state(Medium())
        print("medium speed")


class Medium(State):
    def pull(self, wrapper: Chain):
        wrapper.set_state(High())
        print("high speed")


class High(State):
    def pull(self, wrapper: Chain):
        pass


def main():
    chain = Chain()
    while True:
        print("Press 'Enter'")
        input()
        chain.pull()


if __name__ == "__main__":
    main()
