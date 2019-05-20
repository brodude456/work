class Osoba:

    def __init__(self,name,age):
        self.__name = name
        self.__age =age


    def __str__(self):
        return self.__name+", "+str(self.__age)


    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self,age):
        if age<0 or age>150:
            print("Greska!")
            return False

        self.__age = age

        return True



fatih = Osoba("Fatih",12)
fahro = Osoba("Fahro",30)
print(fatih)

fatih.age = 99

x = fatih.age
print(x)
