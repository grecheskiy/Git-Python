import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        for key, value in self.__color.items():
            time.sleep(value)
            print(key)
        a.running()


a = TrafficLight({"Красный": 7, "Желтый": 2, "Зеленый": 14})
a.running()
