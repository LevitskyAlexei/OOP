import doctest
# TODO Написать 3 класса с документацией и аннотацией типов

class Plane:
    def __init__(self, color: str, kind: str, position: list):
        if not isinstance(color, str) or not isinstance(kind, str):
            raise TypeError("характеристика должна являться строкой")
        if not isinstance(position, list):
            raise TypeError("Позиция должны задаваться списком")

        for kord in position:
            if not isinstance(kord, (int, float)):
                raise TypeError("координаты должны быть числами")
        self.color = color
        self.kind = kind
        self.position = position

    def fly(self, new_position: list):
        """
        Метод позволяет самолёту летать ,
        а наблюдателю понять положение самолёта
        >>> plane = Plane("gray", "ТУ214", [1, 2, 0])
        >>> plane.fly([6,5,10])
        >>> plane.position == [6,5,10]
        True

        :param new_position:  новая позиция птички
        """
        if not isinstance(new_position, list):
            raise TypeError("Позиция должны задаваться списком")

        for kord in new_position:
            if not isinstance(kord, (int, float)):
                raise TypeError("координаты должны быть числами")
        self.position = new_position

    def take_off(self):
        """
        метод позволяет самолёту взлетать
        >>> plane = Plane("gray", "ТУ214", [1, 2, 0])
        >>> plane.take_off()
        """

        ...
class Phone:
    def __init__(self, make: str, model: str, is_broken: bool):
        if not isinstance(make, str):
            raise TypeError("компания производитель должна являться строкой")
        if not isinstance(model, str):
            raise TypeError("модель должны задаваться строкой")
        if not isinstance(is_broken, bool):
            raise TypeError("переменная is_broken должна иметь тип bool")

        self.make = make
        self.model = model
        self.is_broken = is_broken

    def call_(self):
        """
        Метод позволяет телефону звонить
        >>> phone = Phone("Apple", "Iphone7", True)
        >>> phone.call_()
        """
        if self.is_broken:
            self.repair()

        ...  # реализация звонка

    def repair(self):
        """
        Метод позволяет починить телефон
        >>> car = Phone("Apple", "IPhone7", True)
        >>> car.repair()
        """
        if self.is_broken:
            # телефон надо починить
            ...
            self.is_broken = False
        else:
            raise Exception("невозможно отремонтировать исправный телефон")


class Player:
    def __init__(self, position: str, number: int,):
        if not isinstance(position, str):
            raise TypeError("позиция должена являться строкой")
        if not isinstance(number, int):
            raise TypeError("номер должен являться числом")

        self.position = position
        self.number = number

    def pass_(self):
        """
        метод позволяет игроку отдать пас
        >>> player = Player("FW", 5)
        >>> player.pass_()
        """

        ...

    def shoot(self):
        """
        метод позволяет игроку самостоятельно пробить по мячу
        >>> player = Player("FW", 5)
        >>> player.shoot()
        """

        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
