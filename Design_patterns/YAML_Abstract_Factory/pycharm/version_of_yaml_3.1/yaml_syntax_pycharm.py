import yaml
print(yaml.__version__)


# класс определяющий пользовательский тип данных
class ExampleClass:
    def __init__(self, value):
        print(value)
        self.value = value

    def __str__(self):
        return f'ExampleClass, value: {self.value}'


# функция конструктор для типа данных ExampleClass
def constuctor_example_class(loader, node):
    # получаем данные из yaml
    print(node)
    value = loader.construct_mapping(node)
    print(f'value: {value}, type(value): {type(value)}')
    # необходимо выбрать из полученные данных необходимые
    # для создания экземпляра класса ExampleClass

    return ExampleClass(*value)


# регистрируем конструктор
yaml.add_constructor('!example_class', constuctor_example_class)
# yaml строка
document = """!example_class {'1'}"""
# выполняем загрузку
obj = yaml.load(document, Loader=yaml.Loader)
# выведем на принт полученный объект, ожидаем строку вида
# ExampleClass, value - 5
print(obj)
print('-----------')
document = """!example_class {'5':6}"""
# выполняем загрузку
obj = yaml.load(document, Loader=yaml.Loader)
# выведем на принт полученный объект, ожидаем строку вида
# ExampleClass, value - 5
print(obj)
print('-----------')
document = """!example_class {5}"""
# выполняем загрузку
obj = yaml.load(document, Loader=yaml.Loader)
# выведем на принт полученный объект, ожидаем строку вида
# ExampleClass, value - 5
print(obj)
print('-----------')
document = """!example_class {5: 1}"""     # will be an error without space before 1
# выполняем загрузку
obj = yaml.load(document, Loader=yaml.Loader)
# выведем на принт полученный объект, ожидаем строку вида
# ExampleClass, value - 5
print(obj)