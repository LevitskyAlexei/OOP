class Triangle:
    def __init__(self, sides: list[int]):
        """
       Создание и подготовка к работе объекта "Triangle"
        :param sides: Список с длинами сторон треугольника
        """
        self.sides = sides

    @property
    def sides(self) -> list[int]:
        """Вовзвращает список сторон треугольника"""
        return self._sides

    @sides.setter
    def sides(self, sides: list[int]):
        """
        Проверка введенных данных для сторон треугольника
        :param sides: Список с длинами сторон треугольника
        """
        if not isinstance(sides, list):
            raise TypeError("Длины сторон задаются списком")
        if len(sides) != 3:
            raise ValueError("Длина списка сторон должна быть равна 3")
        if not all(isinstance(side, int) for side in sides):
            raise TypeError("Длина каждой стороны задается целым числом")
        self._sides = sides

    def perimeter(self) -> int:
        """
        Нахождение периметра треугольника
        :return:  значение периметра треугольника
        """
        return sum(self.sides)

    def area(self):
        """Нахождение площади треугольника"""
        ...

    def __str__(self):
        return f"{self.__class__.__name__} со сторонами {self.sides!r}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.sides!r})"


class Right(Triangle):
    def __init__(self, leg1: int, leg2: int, hypotenuse: int):
        """
        Создание и подготовка к работе объекта "Right"
        :param leg1, leg2, hypotenuse: длины сторон треугольника
        """
        super().__init__([leg1, leg2, hypotenuse])

    @property
    def leg1(self) -> int:
        """Возвращает длину стороны треугольника"""
        return self.sides[0]

    @leg1.setter
    def leg1(self, new_length1: int):
        """
        изменение длины стороны треугольника
        :param new_length1: новое значение длины стороны треугольника
        """
        self.sides = [new_length1] * 3

    @property
    def leg2(self) -> int:
        return self.sides[0]

    @leg2.setter
    def leg2(self, new_length2: int):
        """
        изменение длины стороны треугольника
        :param new_length2: новое значение длины стороны треугольника
        """
        self.sides = [new_length2] * 2

    @property
    def hypotenuse(self) -> int:
        return self.sides[0]

    @hypotenuse.setter
    def hypotenuse(self, new_lehgth3: int):
        """""
        изменение длины стороны треугольника
        :param new_lehgth3: новое значение длины стороны треугольника
        """""
    def area(self) -> int:
        """
        нахождение площади треугольника
        :return: площадь треугольника
        """
        return self.leg1 * self.leg2

    def __repr__(self):
        return f"{self.__class__.__name__}({self.leg1!r},{self.leg2!r},{self.hypotenuse!r})"


if __name__ == "__main__":
    # Write your solution here
    tr_ = Triangle([1, 2, 3])
    print(tr_)
    print(repr(tr_))
    print(tr_.perimeter())
    print(tr_.area())

    tr_Right = Right(3, 4, 5)
    print(tr_Right)
    print(repr(tr_Right))
    print(tr_Right.perimeter())
    print(tr_Right.area())

