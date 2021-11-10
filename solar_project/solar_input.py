# coding: utf-8
# license: GPLv3

from solar_model import Celestial
from solar_vis import calculate_scale_factor


def open_file():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    in_filename = "solar_system.txt"
    space_objects = __read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
    print(max_distance)
    calculate_scale_factor(max_distance)
    return space_objects


def __read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star" or object_type == "planet":
                celestial = Celestial()
                __parse_celestial_parameters(line, celestial, object_type)
                objects.append(celestial)
            else:
                print("Unknown space object")

    return objects


def __parse_celestial_parameters(line, celestial, type):
    """Считывает данные о небесном теле из строки.

    Входная строка должна иметь слеюущий формат:

    Celestial <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты тела, (Vx, Vy) — скорость.

    Пример строки:

    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описанием тела.

    **celestial** — объект небесное тело.

    **type** - тип небесного тела.
    """

    tokens = line.split()
    assert(len(tokens) == 8)
    celestial.type = type
    celestial.R = int(tokens[1])
    celestial.color = tokens[2]
    celestial.m = float(tokens[3])
    celestial.x = float(tokens[4])
    celestial.y = float(tokens[5])
    celestial.Vx = float(tokens[6])
    celestial.Vy = float(tokens[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME!


if __name__ == "__main__":
    print("This module is not for direct call!")
