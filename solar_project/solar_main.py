# coding: utf-8
# license: GPLv3

from solar_vis import *
from solar_model import init, tick
from solar_input import open_file
import thorpy
import time
import numpy as np

timer = None
alive = True

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

time_scale = 1000.0
"""Шаг по времени при моделировании.
Тип: float"""



def start_execution():
    """Обработчик события нажатия на кнопку Play/Pause.
    Запускает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = True
    


def pause_execution():
    global perform_execution
    perform_execution = False


def stop_execution():
    """Обработчик события нажатия на кнопку Start.
    Останавливает циклическое исполнение функции execution.
    """
    global alive
    alive = False


def activate():
    init(open_file())


def handle_events(events, menu):
    global alive
    for event in events:
        menu.react(event)
        if event.type == pg.QUIT:
            alive = False


def slider_to_real(val):
    return np.exp(5 + val)


def slider_reaction(event):
    global time_scale
    time_scale = slider_to_real(event.el.get_value())


def init_ui(screen):
    global button_play
    slider = thorpy.SliderX(100, (-10, 10), "Simulation speed")
    slider.user_func = slider_reaction
    button_stop = thorpy.make_button("Quit", func=stop_execution)
    button_pause = thorpy.make_button("Pause", func=pause_execution)
    button_play = thorpy.make_button("Play", func=start_execution)
    timer = thorpy.OneLineText("Seconds passed")

    button_load = thorpy.make_button(text="Load a file", func=activate)

    box = thorpy.Box(elements=[
        slider,
        button_pause,
        button_stop, 
        button_play, 
        button_load,
        timer])
    reaction1 = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                reac_func=slider_reaction,
                                event_args={"id": thorpy.constants.EVENT_SLIDE},
                                params={},
                                reac_name="slider reaction")
    box.add_reaction(reaction1)
    
    menu = thorpy.Menu(box)
    for element in menu.get_population():
        element.surface = screen

    box.set_topleft((0, 0))
    box.blit()
    box.update()
    return menu, box, timer


def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    global perform_execution
    global timer

    print('Modelling started!')

    pg.init()
    
    width = 1000
    height = 900
    screen = pg.display.set_mode((width, height))
    last_time = time.perf_counter()
    drawer = Drawer(screen)
    menu, box, timer = init_ui(screen)

    while alive:
        handle_events(pg.event.get(), menu)
        cur_time = time.perf_counter()
        if perform_execution:
            text = "%d seconds passed" % (int(tick((cur_time - last_time) * time_scale)))
            timer.set_text(text)

        last_time = cur_time
        drawer.update(box)
        time.sleep(1.0 / 60)

    print('Modelling finished!')


if __name__ == "__main__":
    main()
