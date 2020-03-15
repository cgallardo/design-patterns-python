import abc


class Employee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def show_employee_details(self):
        pass


class Developer(Employee):
    def __init__(self, identifier: int, name: str, position: str):
        self._identifier = identifier
        self._name = name
        self._position = position

    def show_employee_details(self):
        print("{}: {} ({})".format(self._identifier, self._name, self._position))


class Manager(Employee):
    def __init__(self, identifier: int, name: str, position: str):
        self._identifier = identifier
        self._name = name
        self._position = position

    def show_employee_details(self):
        print("{}: {} ({})".format(self._identifier, self._name, self._position))


class CompanyDirectory(Employee):
    def __init__(self):
        self._employee_list = []

    def add_employee(self, employee: Employee):
        self._employee_list.append(employee)

    def show_employee_details(self):
        for employee in self._employee_list:
            employee.show_employee_details()


def company():
    dev1 = Developer(100, "Mark Lopez", "Sr. Software Engineer")
    dev2 = Developer(101, "Laura Norton", "Sr. Frontend Engineer")
    dev_directory = CompanyDirectory()
    dev_directory.add_employee(dev1)
    dev_directory.add_employee(dev2)

    man1 = Manager(200, "Sara Miller", "CMO")
    man2 = Manager(201, "Bruno Thompson", "CPO")
    man_directory = CompanyDirectory()
    man_directory.add_employee(man1)
    man_directory.add_employee(man2)

    company_directory = CompanyDirectory()
    company_directory.add_employee(dev_directory)
    company_directory.add_employee(man_directory)
    company_directory.show_employee_details()


if __name__ == "__main__":
    company()
