import abc
import random
# from typing import final


class CaffeineBeverage(metaclass=abc.ABCMeta):
    # This should be final -> Python 3.8
    def prepareRecipe(self) -> None:
        self._boil_water()
        self._brew()
        self._pour_in_cup()
        self._add_condiments()

    def _boil_water(self) -> None:
        print("Boiling water...")

    @abc.abstractmethod
    def _brew(self) -> None:
        pass

    @abc.abstractmethod
    def _add_condiments(self) -> None:
        pass

    def _pour_in_cup(self) -> None:
        print("Pouring into cup...")


class CaffeineBeverageWithHook(metaclass=abc.ABCMeta):
    # This should be final -> Python 3.8
    def prepareRecipe(self) -> None:
        self._boil_water()
        self._brew()
        self._pour_in_cup()
        if self._customer_wants_condiments():
            self._add_condiments()

    def _boil_water(self) -> None:
        print("Boiling water...")

    @abc.abstractmethod
    def _brew(self) -> None:
        pass

    @abc.abstractmethod
    def _add_condiments(self) -> None:
        pass

    def _pour_in_cup(self) -> None:
        print("Pouring into cup...")

    def _customer_wants_condiments(self) -> bool:
        return True


class Coffee(CaffeineBeverage):
    def _brew(self) -> None:
        print("Dripping coffee through filter...")

    def _add_condiments(self) -> None:
        print("Adding sugar and milk...")


class Tea(CaffeineBeverage):
    def _brew(self) -> None:
        print("Steeping the tea...")

    def _add_condiments(self) -> None:
        print("Adding lemon...")


class CoffeeWithHook(CaffeineBeverageWithHook):
    def _brew(self) -> None:
        print("Dripping coffee through filter...")

    def _add_condiments(self) -> None:
        print("Adding sugar and milk...")

    def _customer_wants_condiments(self) -> bool:
        x = random.randrange(0, 2)

        return x == 1


class TeaWithHook(CaffeineBeverageWithHook):
    def _brew(self) -> None:
        print("Steeping the tea...")

    def _add_condiments(self) -> None:
        print("Adding lemon...")

    def _customer_wants_condiments(self) -> bool:
        x = random.randrange(0, 2)

        return x == 1


def main():
    tea_with_hook = TeaWithHook()
    coffee_with_hook = CoffeeWithHook()

    print("Making tea: ")
    tea_with_hook.prepareRecipe()

    print("Making coffee: ")
    coffee_with_hook.prepareRecipe()


if __name__ == "__main__":
    main()
