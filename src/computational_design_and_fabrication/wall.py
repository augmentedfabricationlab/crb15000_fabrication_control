import math
import compas

from compas.datastructures import Mesh
from window_in_wall import Wall
import itertools


class Wall_ProjectTitle(Wall):
    """Wall generator"""

    def __init__(self):
        """Constructor"""
        super(Wall_ProjectTitle, self).__init__()

    def sample_definition(self, foo):
        """Adding new definitions to the class"""
        bar = foo + 'bar'
        return bar

    def sin_wave(self, amp, freq, phase, value):
        """Manipulating existing functions"""
        phase = phase + math.pi
        return(amp * math.sin(2.0 * math.pi * freq * value + phase))
