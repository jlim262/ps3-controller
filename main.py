
from ps3_controller import PS3Controller
from event_handler import EventHandler


class MyHandler(EventHandler):
    def __init__(self):
        super().__init__()

    def handle_x(self):
        return {'stop':True}


if __name__ == "__main__":
    handler = MyHandler()
    controller = PS3Controller(handler)
    controller.run()
    print('Program is stopped')
