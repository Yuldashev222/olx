from enum import Enum


class Licences(Enum):
    a = 'A'
    b = 'B'
    c = 'C'
    d = 'D'
    b_e = 'B+E'
    c_e = 'c+E'
    d_e = 'D+E'
    yoq = 'YOQ'

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)

class LanguageLevel(Enum):
    il = 'Ilg\'or'
    bo = 'Boshlang\'ich'
    er = 'Erkin'
    orta = 'O\'rta'

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)
