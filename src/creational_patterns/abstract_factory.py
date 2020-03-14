import abc


class Dough(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def price(self) -> int:
        pass

    @abc.abstractmethod
    def is_crust_stuffed(self) -> bool:
        pass


class Sauce(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def price(self) -> int:
        pass

    @abc.abstractmethod
    def is_spicy(self) -> bool:
        pass


class PizzaIngredientFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abc.abstractmethod
    def create_sauce(self) -> Sauce:
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThickCrustDough()

    def create_sauce(self) -> Sauce:
        return PlumTomatoSauce()


class ThinCrustDough(Dough):
    def price(self) -> int:
        return 200

    def is_crust_stuffed(self) -> bool:
        return False

    def __str__(self) -> str:
        return "Thin crust"


class ThickCrustDough(Dough):
    def price(self) -> int:
        return 300

    def is_crust_stuffed(self) -> bool:
        return True

    def __str__(self) -> str:
        return "Thick crust stuffed with cheese"


class MarinaraSauce(Sauce):
    def price(self) -> int:
        return 100

    def is_spicy(self) -> bool:
        return False

    def __str__(self) -> str:
        return "Marinara sauce"


class PlumTomatoSauce(Sauce):
    def price(self) -> int:
        return 150

    def is_spicy(self) -> bool:
        return False

    def __str__(self) -> str:
        return ""


def pizza_store():
    for factory in (NYPizzaIngredientFactory(), ChicagoPizzaIngredientFactory()):
        dough = factory.create_dough()
        sauce = factory.create_sauce()
        print("Product: {}".format(dough))
        print("Crust stuffed: {}".format(dough.is_crust_stuffed()))
        print("Price: {}".format(dough.price()))
        print("Product: {}".format(sauce))
        print("Spicy: {}".format(sauce.is_spicy()))
        print("Price: {}".format(sauce.price()))


if __name__ == "__main__":
    pizza_store()
