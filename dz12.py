'''
Создайте класс студента. 
○Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
○Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
'''
import csv


class Name:
    def __init__(self, name):
        self.validate(name)
        self.name = name
       
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')
    
    def validate(self, value):
        if not (value.isalpha()):
            raise TypeError(f'Имя должно состоять только из букв!')
        if not (value.istitle()):
            raise TypeError(f'Имя должно начинаться с большой буквы!')


class Student:
    first_name = None
    second_name = None 

    def __init__(self, name1, name2):
        self.first_name = Name(name1) 
        self.second_name = Name(name2)

        self.marks = {}
        self.tests = {}
        f = open('data.csv', encoding="utf-8")
        reader = csv.reader(f)
        for i in reader:
            self.marks[i[0]] = None
            self.tests[i[0]] = None
        f.close()
        
    def __str__(self):
        return f'Student(first_name={self.first_name}, second_name={self.second_name}'
    
    def set_marks(self, subject, my_list):
        self.marks[subject] = my_list

    def set_tests(self, subject, my_list):
        self.tests[subject] = my_list   


    def average_test(self, subject):
        sum = 0
        counter = 0
        for m in self.tests[subject]:
            sum += m
            counter += 1 

        return round(sum / counter, 2)    
    
    def average_total(self):
        sum = 0
        counter = 0  # for key in currencies.keys():
        for key in self.marks.keys():
            if self.marks[key]:
                for m in self.tests[key]:
                    sum += m
                    counter += 1 
        return round(sum / counter, 2)    
    
 
if __name__ == '__main__':
    std_one = Student('Иван', 'Ильин')
    std_one.set_marks("физика", [5, 5, 4])
    std_one.set_tests("физика", [5, 4, 4])
    std_one.set_marks("математика", [3, 5, 5, 4])
    std_one.set_tests("математика", [2, 3, 5, 4, 4])
    std_one.set_marks("русский", [5, 5, 5, 4, 5])
    std_one.set_tests("русский", [5, 4, 4])
    print(std_one.marks)
    print(std_one.tests)
    print(std_one.average_test("физика"))
    print(std_one.average_total())

    #std_second = Student('Мария', 'кузьмина')
    #std_three = Student('34fg', 'Ильин')
   
