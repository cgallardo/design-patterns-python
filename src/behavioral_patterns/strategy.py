import abc


class QuackBehaviour(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self):
        pass


class FlyBehaviour(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(self):
        pass


class Quack(QuackBehaviour):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehaviour):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehaviour):
    def quack(self):
        print("Squeak")


class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("I cannot fly")


class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("I am flying")


class Duck(metaclass=abc.ABCMeta):
    _fly_behaviour = None
    _quack_behaviour = None

    @abc.abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self._fly_behaviour.fly()

    def perform_quack(self):
        self._quack_behaviour.quack()

    def swim(self):
        print("All ducks float, even decoys")

    def setFlyBehavior(self, fly_behavior: FlyBehaviour):
        self._fly_behaviour = fly_behavior

    def setQuackBehaviour(self, quack_behaviour: QuackBehaviour):
        self._quack_behaviour = quack_behaviour


class MallardDuck(Duck):
    def __init__(self):
        self._quack_behaviour = Quack()
        self._fly_behaviour = FlyWithWings()

    def display(self):
        print("I am a mallard duck")


class WoodenDuck(Duck):
    def __init__(self):
        self._quack_behaviour = MuteQuack()
        self._fly_behaviour = FlyNoWay()

    def display(self):
        print("I am a decoy")


def main():
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()
    mallard.setFlyBehavior(FlyNoWay())
    mallard.perform_quack()
    mallard.perform_fly()
    mallard.swim()
    mallard.display()


if __name__ == "__main__":
    main()
