import numpy as np
from colors import standard, alternative


class Vortex:
    def __init__(self, pos, circulation, velocity=(0, 0)):
        self.pos = pos
        self.circulation = circulation
        self.velocity = velocity

    @property
    def color(self):
        """Get the display colour of the vortex, indicating its circulation."""
        if self.circulation > 0:
            return standard.correct_gamma(np.abs(self.circulation))
        else:
            return alternative.correct_gamma(np.abs(self.circulation))

    def outOfBounds(self):
        """Return whether the vortex has completely left the screen."""
        self_x, self_y = self.pos
        return abs(self_x) > 10000 or abs(self_y) > 10000

    # The functions to be filled in:

    def getInducedVelocity(self, other_pos):
        """Get the velocity induced at other_pos by the vortex, as a tuple."""

    def computeVelocity(self, vortexArray):
        """
        Compute the velocity of the vortex by combining the contributions from
        all surrounding vortices.
        """

    def move(self, timePeriod):
        """
        Move the vortex over the specified time period.
        """
