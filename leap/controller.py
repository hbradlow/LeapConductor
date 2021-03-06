from lib import Leap
from abletonactions import *

from tempo import TempoListener
from startgesture import *
from testlistener import *
from tracklistener import *

from MidiInterface import *
import threading, time

# Query gesture information and communicate with Ableton
# to control music

class AbletonController:
    """
    """
    supported_gestures = {
        'tempoChange': (tempoChangeAction, TempoListener),
        'stopTrack': (trackStopAction, StopTrackListener),
        'lowerVolume': (lowerVolumeAction, LowerVolumeListener),
        'raiseVolume': (raiseVolumeAction, RaiseVolumeListener),
        'startTrack': (trackStartAction, StartTrackListener),
        'trackDown': (trackDownAction, TrackDownListener),
        'trackUp': (trackUpAction, TrackUpListener),
        #'test': (trackStartAction, TestListener)
    }


    def __init__(self):
        self.midi_interface = MidiInterface()
        self.recognizers = []
        self.controllers = []

        self.current_vol = 90
        self.stopped = False
        self.current_track = 1
        self.delay = 2.0
        self.track_count = 3
        self.tempo_count = 0

        self.track_updates = {'up':time.time(), 'down':time.time()}

        for g_name in AbletonController.supported_gestures.keys():
            callback = AbletonController.supported_gestures[g_name][0]
            recognizer = AbletonController.supported_gestures[g_name][1]

            r = recognizer(callback, self)
            self.recognizers.append(r)
            self.controllers.append(Leap.Controller(r))
            print "Initialized a recognizer for %s" % g_name

    def destroy(self):
        self.controllers = None

    def canUpTrack(self):
        return time.time() - self.track_updates['up'] > self.delay

    def canDownTrack(self):
        return time.time() - self.track_updates['down'] > self.delay

    def trackUp(self):
        if self.canUpTrack() and self.current_track < self.track_count:
            self.current_track += 1
            self.track_updates['up'] = time.time()
            self.tempo_count = 0

    def trackDown(self):
        if self.canDownTrack() and self.current_track > 1:
            self.current_track -= 1
            self.track_updates['down'] = time.time()
            self.tempo_count = 0

    def canTempo(self):
        return self.can_tempo > 1

    def setMidi(self, bpm):
        self.tempo_count += 1
        if self.canTempo():
            print 'updating tempo'
            self.midi_interface.set_tempo(bpm)
