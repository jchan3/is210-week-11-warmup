#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_04."""


import car


class CustomCar(car.Car):
    """A subclass of the Car class."""

    def __init__(self, color='red', tires=None):
        """Constructor for the Car() class.

        Args:
            color (string): The color of the car. Defaults to ``'red'``.
            tires (list): A list of CustomTire() objects. Defaults to None.

        Attributes:
            color (string): The color of the car.
            tires (list): A list of CustomTire() objects.
        """
        car.Car.__init__(self, color)

        if tires is None:
            tires = []
            tire1 = CustomTire()
            tires.append(tire1)
            tire2 = CustomTire()
            tires.append(tire2)
            tire3 = CustomTire()
            tires.append(tire3)
            tire4 = CustomTire()
            tires.append(tire4)

        self.tires = tires


class CustomTire(car.Tire):
    """A subclass of the Tire class."""

    def __init__(self, miles=0):
        """Constructor for the CustomTire() class.

        Args:
            miles (integer): The number of miles on the Tire. Defaults to 0.

        Attributes:
           miles (integer): The number of miles on the Tire.
           maximum_miles (integer): A pseudo_private class attribute for
               the maximum miles on a tire.
        """
        car.Tire.__init__(self, miles)
        self.__maximum_miles = 500
