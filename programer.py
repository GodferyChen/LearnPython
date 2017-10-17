class Programer(object):
    hobby = 'Play computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print('My name is %s \nI am %s years old\n' % (self.name, self._age))


class BackendProgramer(Programer):
    def __init__(self, name, age, weight, language):
        super(BackendProgramer,self).__init__(name,age,weight)
        self.language = language

    def self_introduction(self):
        print('My name is %s \nMy favorite language is %s' % (self.name,self.language))

def introduce(programer):
    if isinstance(programer,Programer):
        programer.self_introduction()


if __name__ == '__main__':
    programer = Programer('Tim',23,120)
    backend_programer = BackendProgramer("Raki", 25, 130,'Python')
    introduce(programer)
    introduce(backend_programer)
