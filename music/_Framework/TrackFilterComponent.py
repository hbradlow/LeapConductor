# emacs-mode: -*- python-*-
import Live
from _Generic.Devices import *
from ControlSurfaceComponent import ControlSurfaceComponent
from EncoderElement import EncoderElement
FILTER_DEVICES = {'AutoFilter': {'Frequency': 'Frequency',
                'Resonance': 'Resonance'},
 'Operator': {'Frequency': 'Filter Freq',
              'Resonance': 'Filter Res'},
 'OriginalSimpler': {'Frequency': 'Filter Freq',
                     'Resonance': 'Filter Res'},
 'MultiSampler': {'Frequency': 'Filter Freq',
                  'Resonance': 'Filter Res'},
 'UltraAnalog': {'Frequency': 'F1 Freq',
                 'Resonance': 'F1 Resonance'},
 'StringStudio': {'Frequency': 'Filter Freq',
                  'Resonance': 'Filter Reso'}}
class TrackFilterComponent(ControlSurfaceComponent):
    __module__ = __name__
    __doc__ = " Class representing a track's filter, attaches to the last filter in the track "

    def __init__(self):
        ControlSurfaceComponent.__init__(self)
        self._track = None
        self._device = None
        self._freq_control = None
        self._reso_control = None



    def disconnect(self):
        if (self._freq_control != None):
            self._freq_control.release_parameter()
            self._freq_control = None
        if (self._reso_control != None):
            self._reso_control.release_parameter()
            self._reso_control = None
        if (self._track != None):
            self._track.remove_devices_listener(self._on_devices_changed)
            self._track = None
        self._device = None



    def on_enabled_changed(self):
        self.update()



    def set_track(self, track):
        assert ((track == None) or isinstance(track, Live.Track.Track))
        if (self._track != None):
            self._track.remove_devices_listener(self._on_devices_changed)
            if (self._device != None):
                if (self._freq_control != None):
                    self._freq_control.release_parameter()
                if (self._reso_control != None):
                    self._reso_control.release_parameter()
        self._track = track
        if (self._track != None):
            self._track.add_devices_listener(self._on_devices_changed)
        self._on_devices_changed()



    def set_filter_controls(self, freq, reso):
        assert isinstance(freq, EncoderElement)
        assert isinstance(freq, EncoderElement)
        if (self._device != None):
            if (self._freq_control != None):
                self._freq_control.release_parameter()
            if (self._reso_control != None):
                self._reso_control.release_parameter()
        self._freq_control = freq
        self._reso_control = reso
        self.update()



    def update(self):
        if (self.is_enabled() and (self._device != None)):
            device_dict = FILTER_DEVICES[self._device.class_name]
            if (self._freq_control != None):
                self._freq_control.release_parameter()
                parameter = get_parameter_by_name(self._device, device_dict['Frequency'])
                if (parameter != None):
                    self._freq_control.connect_to(parameter)
            if (self._reso_control != None):
                self._reso_control.release_parameter()
                parameter = get_parameter_by_name(self._device, device_dict['Resonance'])
                if (parameter != None):
                    self._reso_control.connect_to(parameter)
        self._rebuild_callback()



    def _on_devices_changed(self):
        self._device = None
        if (self._track != None):
            for index in range(len(self._track.devices)):
                device = self._track.devices[(-1 * (index + 1))]
                if (device.class_name in FILTER_DEVICES.keys()):
                    self._device = device
                    break

        self.update()




# local variables:
# tab-width: 4
