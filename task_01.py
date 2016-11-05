#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_01."""


import produce


TOMATO = produce.Produce()
EGGPLANT = produce.Produce(1311210802)

TOMATO_ARRIVAL = TOMATO.arrival
EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
