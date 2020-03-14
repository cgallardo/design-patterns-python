class Singleton:
    _unique_instance = None

    @staticmethod
    def get_instance():
        if Singleton._unique_instance is None:
            Singleton._unique_instance = Singleton()

        return Singleton._unique_instance


def main():
    m1 = Singleton.get_instance()
    m2 = Singleton.get_instance()
    print(m1, m2)
    assert m1 is m2


if __name__ == "__main__":
    main()
