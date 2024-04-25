# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, name, ID):
        self.__name = name
        self.__ID = ID
        self.__level = "user"
    def set_name(self, name):
        self.__name = name
    def set_ID(self, ID):
        self.__ID = ID
    def getInfo(self):
        print(self.__level, self.__name, self.__ID)
    def getID(self):
        return self.__ID

class Admin(User):
    def __init__(self,name, ID):
        super().__init__(name, ID)
        self.__level = "admin"
    def add_user(self, userList, name, ID):
        u = User(name, ID)
        userList.append(u)
        print("Пользователь с ID " + str(ID) + " добавлен")
        return userList
    def remove_user(self, userList, ID):
        done = False
        for u in userList:
            if u.getID() == ID:
                userList.remove(u)
                done = True

        if done == False:
            print("Пользователь с ID "+ str(ID)+" не найден")
        else:
            print("Пользователь с ID "+ str(ID)+" удален")
        return userList

TekuserList = list()
AdminUser = Admin("Вася", 1)


AdminUser.add_user(TekuserList, "Маша", 2)
AdminUser.add_user(TekuserList, "Петя", 3)
AdminUser.remove_user(TekuserList, 2)
