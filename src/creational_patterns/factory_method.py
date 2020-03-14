import abc


class Pizza(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def price(self) -> int:
        pass


class PizzaStore(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        if "cheese" == pizza_type:
            return NYStyleCheesePizza()
        elif "pepperoni" == pizza_type:
            return NYStylePepperoniPizza()
        else:
            raise NotImplemented()


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        if "cheese" == pizza_type:
            return ChicagoStyleCheesePizza()
        elif "pepperoni" == pizza_type:
            return ChicagoStylePepperoniPizza()
        else:
            raise NotImplemented()


class NYStyleCheesePizza(Pizza):
    def price(self) -> int:
        return 850

    def __str__(self) -> str:
        return "NY Style Cheese Pizza"


class NYStylePepperoniPizza(Pizza):
    def price(self) -> int:
        return 1050

    def __str__(self) -> str:
        return "NY Style Pepperoni Pizza"


class ChicagoStyleCheesePizza(Pizza):
    def price(self) -> int:
        return 750

    def __str__(self) -> str:
        return "Chicago Style Cheese Pizza"


class ChicagoStylePepperoniPizza(Pizza):
    def price(self) -> int:
        return 950

    def __str__(self) -> str:
        return "Chicago Style Pepperoni Pizza"


def pizza_store_app():
    concrete_store = NYPizzaStore()
    pizza = concrete_store.create_pizza("cheese")
    print("Product: {}".format(pizza))
    print("Price: {}".format(pizza.price()))

    concrete_store = ChicagoPizzaStore()
    pizza = concrete_store.create_pizza("pepperoni")
    print("Product: {}".format(pizza))
    print("Price: {}".format(pizza.price()))


if __name__ == "__main__":
    pizza_store_app()
