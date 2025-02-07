"""
A package for working with arrays
"""


class Converter:
    @staticmethod
    def list_to_tuple(array: list):
        return tuple(array)

    @staticmethod
    def tuple_to_list(array: tuple):
        return list(array)


class Finder:
    @staticmethod
    def find_max_and_min(array: list | tuple):
        if not isinstance(array, (list, tuple)):
            raise TypeError("Input is not a list or tuple")

        if not all(isinstance(item, (int, float)) for item in array):
            raise TypeError("Array must contain only integers or floats")

        return max(array), min(array)

    @staticmethod
    def find_integers(array: list | tuple):
        if not isinstance(array, (list, tuple)):
            raise TypeError("Input is not a list or tuple")

        return [item for item in array if isinstance(item, int)]

    @staticmethod
    def find_floats(array: list | tuple):
        if not isinstance(array, (list, tuple)):
            raise TypeError("Input is not a list or tuple")

        return [item for item in array if isinstance(item, float)]

    @staticmethod
    def find_strings(array: list | tuple):
        if not isinstance(array, (list, tuple)):
            raise TypeError("Input is not a list or tuple")

        return [item for item in array if isinstance(item, str)]

    @staticmethod
    def find_booleans(array: list | tuple):
        if not isinstance(array, (list, tuple)):
            raise TypeError("Input is not a list or tuple")

        return [item for item in array if isinstance(item, bool)]