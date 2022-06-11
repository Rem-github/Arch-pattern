from abc import ABC, abstractmethod


class AbstractCourseFactory(ABC):

    @abstractmethod
    def create_online_course(self):
        pass

    @abstractmethod
    def create_offline_course(self):
        pass


class OfflineCourse(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class OnlineCourse(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Python(AbstractCourseFactory):

    def __init__(self, name, address, start_date, teachers_name, students):
        self.name = name
        self.address = address
        self.start_date = start_date
        self.teachers_name = teachers_name
        self.students = students


    def create_online_course(self):
        return PythonOnlineCourse('Питон онлайн', 'www.my_site.ru/python/web_course', self.start_date)

    def create_offline_course(self):
        return PythonOfflineCourse('Питон для всех', 'Москва, ул.Ленина, д.100', self.start_date)


class Java(AbstractCourseFactory):

    def __init__(self, start_date):
        self.start_date = start_date


    def create_online_course(self):
        return JavaOnlineCourse('Java онлайн', 'www.my_site.ru/java/web_course', self.start_date)

    def create_offline_course(self):
        return JavaOnlineCourse('Java для всех', 'Москва, ул.Ленина, д.100', self.start_date)


class PythonOnlineCourse(OnlineCourse):

    def start(self):
        print('Начался курс Питон онлайн')

    def stop(self):
        print('Закончился курс Питон онлайн')


class PythonOfflineCourse(OfflineCourse):

    def start(self):
        print('Начался курс Питон для всех')

    def stop(self):
        print('Закончился курс Питон для всех')


class JavaOnlineCourse(OnlineCourse):

    def start(self):
        print(f'Курс Java онлайн начнется {self.start_date}')

    def stop(self):
        print('Закончился курс Java онлайн')


class JavaOfflineCourse(OfflineCourse):

    def start(self):
        print('Начался курс Java для всех')

    def stop(self):
        print('Закончился курс Java для всех')


class FabricCourses:
    PYTHON = 'python'
    JAVA = 'java'

    @classmethod
    def create_course(cls, lang, start_date):
        if lang == cls.PYTHON:
            return Python(start_date)
        elif lang == cls.JAVA:
            return Java(start_date)
        

class User(ABC):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @abstractmethod
    def join_course(self):
        pass

    @abstractmethod
    def leave_course(self):
        pass


class Student(User):

    def join_course(self):
        pass

    def leave_course(self):
        pass

class Teacher(User):

    def join_course(self):
        pass

    def leave_course(self):
        pass





fabric = FabricCourses.create_course('java', '01.07.2022')
course1 = fabric.create_online_course()

