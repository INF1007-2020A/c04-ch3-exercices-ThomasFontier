#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return a*a

def average(a: float, b: float, c: float) -> float:
    z = a+b+c
    return z/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    z = angle_degs + angle_mins/60 + angle_secs/3600
    return math.radians(z)


def to_degrees(angle_rads: float) -> tuple:
    z = math.degrees(angle_rads)
    deg = int(z)
    z_2 = (z-deg)*60
    min = int(z_2)
    sec = (z_2-min)*60
    return deg, min, int(sec)


def to_celsius(temperature: float) -> float:
    z = temperature-32
    return z/1.8


def to_farenheit(temperature: float) -> float:
    z = 1.8*temperature
    return z+32


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
