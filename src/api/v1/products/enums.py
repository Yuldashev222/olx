from enum import Enum

class Status(Enum):
    y = 'Yangi'
    j = 'Jarayonda'
    r = 'Rad etildi'
    t = 'Tastiqlandi'

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)

class ValueType(Enum):
    n = 'Narx'
    b = 'Bepul'
    a = 'Ayirboshlash'

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)