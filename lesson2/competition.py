from random import randint


class Competition:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, distance):
        self.__distance = distance

    def start(self, competitors, weather):
        for competitor_name in competitors:
            competitor_time = 0
            car = competitors[competitor_name]

            for distance in range(self.__distance):
                _wind_speed = randint(0, weather.wind_speed)

                if competitor_time == 0:
                    _speed = 1
                else:
                    _speed = (competitor_time / car.time_to_max) * car.max_speed
                    if _speed > _wind_speed:
                        _speed -= (car.drag_coef * _wind_speed)

                competitor_time += float(1) / _speed

            print("Car <%s> result: %f" % (competitor_name, competitor_time))
