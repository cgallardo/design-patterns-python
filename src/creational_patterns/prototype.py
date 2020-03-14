import sys
import copy


class Person:
    _name = ""

    def __str__(self) -> str:
        return self._name


class Tom(Person):
    _name = "Tom"


class Mark(Person):
    _name = "Mark"


class Harry(Person):
    _name = "Harry"


class Factory:
    _prototypes = {
        "tom": Tom(),
        "mark": Mark(),
        "harry": Harry(),
    }

    @staticmethod
    def get_prototype(person_type: str) -> Person:
        prototype = Factory._prototypes.get(person_type)
        if prototype:
            return copy.deepcopy(prototype)


def main():
    if len(sys.argv) > 1:
        for person_name in sys.argv[1:]:
            person = Factory.get_prototype(person_name)
            if person is not None:
                print(person)
    else:
        print("Run again with arguments")


if __name__ == "__main__":
    main()



