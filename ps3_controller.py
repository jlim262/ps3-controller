
import pygame
from gpiozero import Servo


class PS3Controller(object):
    def __init__(self, event_handler, log_print=True):
        pygame.init()
        self.joystick = self.get_joystick()
        self.event_handler = event_handler
        self.btn_idx = {
            'x': 0, 'circle': 1, 'triangle': 2, 'square': 3,
            'l1': 4, 'r1': 5, 'l2': 6, 'r2': 7,
            'select': 8, 'start': 9, 'ps': 10, 'l3': 11, 'r3': 12,
            'up': 13, 'down': 14, 'left': 15, 'right': 16}
        self.stop = False
        self.log_print = log_print
        self.status = ''

    def print_status(self):
        assert (self.joystick is not None)

        pygame.event.pump()
        output = '('
        for i in range(5):
            if i == 2:
                continue
            v = self.joystick.get_axis(i)
            output += f'{v: .4f}' + ' '
        output += ')'

        numbuttons = self.joystick.get_numbuttons()
        for i in range(numbuttons):
            v = self.joystick.get_button(i)
            output += str(i) + f':{v}' + '|'

        if self.status != output:
            print(output)
            self.status = output

    def get_joystick(self):
        if not pygame.joystick.get_init():
            pygame.joystick.init()

        joysticks = [pygame.joystick.Joystick(
            x) for x in range(pygame.joystick.get_count())]

        if len(joysticks) < 1:
            raise IOError(
                'No Playstation controller is found. Please check whether the controller is connected correctly.')

        for joystick in joysticks:
            if 'playstation' in joystick.get_name().lower():
                name = joystick.get_name()
                print(f'{name} is found.')
                joystick.init()

                numaxes = joystick.get_numaxes()
                numbuttons = joystick.get_numbuttons()

                if numaxes > 0 and numbuttons > 0:
                    print(f'{name} has {numaxes} axies and {numbuttons} buttons')
                    return joystick

        raise IOError('No Playstation controller is found.')

    def update(self):
        assert (self.joystick is not None)

        try:
            pygame.event.pump()

            self.event_handler.registered_event

            for k, fn in self.event_handler.registered_event.items():
                if (k == 'stick'):
                    axies = (self.joystick.get_axis(0), self.joystick.get_axis(
                        1), self.joystick.get_axis(3), self.joystick.get_axis(4))
                    func = getattr(self.event_handler, fn)
                    func(axies)
                else:
                    btn_id = self.btn_idx[k]
                    if self.joystick.get_button(btn_id) == 1:
                        func = getattr(self.event_handler, fn)
                        r = func()
                        if 'stop' in r:
                            self.stop = r['stop']
        except pygame.error as e:
            print(f'Error while getting joystick button inputs: {e}')

    def run(self):
        while not self.stop:
            if self.log_print:
                self.print_status()
            self.update()
