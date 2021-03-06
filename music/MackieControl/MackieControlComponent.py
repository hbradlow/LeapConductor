# emacs-mode: -*- python-*-
from consts import *
import Live
class MackieControlComponent:
    __module__ = __name__
    __doc__ = "Baseclass for every 'sub component' of the Mackie Control. Just offers some "

    def __init__(self, main_script):
        self._MackieControlComponent__main_script = main_script



    def destroy(self):
        self._MackieControlComponent__main_script = None



    def main_script(self):
        return self._MackieControlComponent__main_script



    def shift_is_pressed(self):
        return self._MackieControlComponent__main_script.shift_is_pressed()



    def option_is_pressed(self):
        return self._MackieControlComponent__main_script.option_is_pressed()



    def control_is_pressed(self):
        return self._MackieControlComponent__main_script.control_is_pressed()



    def alt_is_pressed(self):
        return self._MackieControlComponent__main_script.alt_is_pressed()



    def song(self):
        return self._MackieControlComponent__main_script.song()



    def script_handle(self):
        return self._MackieControlComponent__main_script.handle()



    def application(self):
        return self._MackieControlComponent__main_script.application()



    def send_midi(self, bytes):
        self._MackieControlComponent__main_script.send_midi(bytes)



    def request_rebuild_midi_map(self):
        self._MackieControlComponent__main_script.request_rebuild_midi_map()




# local variables:
# tab-width: 4
