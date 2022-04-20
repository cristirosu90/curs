from abc import abstractmethod

class FormaGeometrica:
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi.')

class Patrat(FormaGeometrica):
    __latura = 14

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def get_latura(self):
        print(f'Getter: Latura patratului este {self.__latura}.')
        return self.__latura

    @latura.setter
    def set_latura(self, latura):
        print(f'Setter: Noua latura a patratului este {latura}.')
        self.__latura = latura

    @latura.deleter
    def del_latura(self):
        print(f'Deleter: Am sters latura.')
        self.__latura = None


p1 = Patrat()
p1.get_latura

