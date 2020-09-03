from abc import ABC, abstractmethod
from types import FunctionType
class Meta(type):
    def __call__(cls, *args, **kwargs):
            funcs = [x for x, y in cls.__dict__.items() if type(y) == FunctionType and not x.startswith('__')]
            instance = super().__call__(*args, **kwargs)
            for f in funcs:
                key = f.replace('handle_', '')
                instance.registered_event[key] = f
            return instance

class EventHandler(object, metaclass=Meta):
    def __init__(self):
        self.registered_event = {}
    
    def register(self, key, fn):
        self.registered_event[key] = fn
    
    def handle_stick(self, axies):
        raise NotImplementedError

    def handle_x(self):
        raise NotImplementedError

    def handle_circle(self):
        raise NotImplementedError

    def handle_triangle(self):
        raise NotImplementedError

    def handle_square(self):
        raise NotImplementedError

    def handle_l1(self):
        raise NotImplementedError

    def handle_l2(self):
        raise NotImplementedError

    def handle_l3(self):
        raise NotImplementedError

    def handle_r1(self):
        raise NotImplementedError

    def handle_r2(self):
        raise NotImplementedError

    def handle_r3(self):
        raise NotImplementedError

    def handle_up(self):
        raise NotImplementedError

    def handle_down(self):
        raise NotImplementedError

    def handle_left(self):
        raise NotImplementedError

    def handle_right(self):
        raise NotImplementedError

    def handle_select(self):
        raise NotImplementedError

    def handle_start(self):
        raise NotImplementedError

    def handle_ps(self):
        raise NotImplementedError



