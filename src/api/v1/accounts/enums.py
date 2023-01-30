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
        return ((_.name, _.value) for _ in cls)
