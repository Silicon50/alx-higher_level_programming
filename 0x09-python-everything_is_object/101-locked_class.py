#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    returns object has no attribute if attributes is not 'first_name'.
    """

    __slots__ = ["first_name"]
