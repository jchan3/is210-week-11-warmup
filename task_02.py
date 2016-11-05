#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_02."""


import time


class Snapshot(object):
    """A generic snapshot class.

    Args:
        None

    Attributes:
        created (numeric): The time the object was created in a Unix timestamp.
    """
    def __init__(self):
        self.created = time.time()
