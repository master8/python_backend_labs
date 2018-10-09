from lesson2.car import Car
from lesson2.competition import Competition
from lesson2.weather import Weather

cars = {
    'ferrary': Car(max_speed=340, drag_coef=0.324, time_to_max=26),
    'bugatti': Car(max_speed=407, drag_coef=0.39, time_to_max=32),
    'toyota': Car(max_speed=180, drag_coef=0.25, time_to_max=40),
    'lada': Car(max_speed=180, drag_coef=0.32, time_to_max=56),
    'sx4': Car(max_speed=180, drag_coef=0.33, time_to_max=44)
}

weather = Weather(wind_speed=20)
competition = Competition(distance=10000)
competition.start(competitors=cars, weather=weather)
