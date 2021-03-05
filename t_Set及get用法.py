class Person(object):

    def __init__(self, name):
        # 以__开头的属性表示私有属性，不允许外部访问
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, newName):
        if len(newName) >= 5:
            self.__name = newName
        else:
            print("Error：输入的名字长度不够")


if __name__ == '__main__':

    xiaoming = Person("Se7eN_HOU")
    print(xiaoming.__name)
