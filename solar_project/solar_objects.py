# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11


class Celestial:
    """Тип данных, описывающий небесное тело.
    Содержит массу, координаты, скорость тела,
    а также визуальный радиус тела в пикселах и его цвет
    """
    def __init__(self):
        self.type = "None"
        self.m = 1
        self.x = 0
        self.y = 0
        self.Vx = 0
        self.Vy = 0
        self.Fx = 0
        self.Fy = 0
        self.R = 5
        self.color = "green"

    def calculate_force(self):
        """Вычисляет силу, действующую на тело.

        Параметры:

        **body** — тело, для которого нужно вычислить дейстующую силу.

        **space_objects** — список объектов, которые воздействуют на тело.
        """

        self.Fx = self.Fy = 0
        for obj in space_objects:
            if self == obj:
                continue  # тело не действует гравитационной силой на само себя!
            r = ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5
            r = max(r, self.R + obj.R) # обработка аномалий при прохождении одного тела сквозь другое
            self.Fx += -gravitational_constant * obj.m * self.m * (self.x - obj.x)/r**3
            self.Fy += -gravitational_constant * obj.m * self.m * (self.y - obj.y)/r**3

    def move(self, dt):
        """Перемещает тело в соответствии с действующей на него силой.

        Параметры:

        **body** — тело, которое нужно переместить.
        """
        ax = self.Fx / self.m
        self.x += self.Vx * dt + ax * dt ** 2 / 2
        self.Vx += ax * dt
        ay = self.Fy / self.m
        self.y += self.Vy * dt + ay * dt ** 2 / 2
        self.Vy += ay * dt