class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_score(self):
        print("%s:%s" % (self.__name, self.__score))


timi = Student("timi", 200)
yang = Student("yang", 100)

timi.get_score()
yang.get_score()
