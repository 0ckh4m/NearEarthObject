"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).
        An NEO encapsulates semantic and physical parameters about the object, suchas its primary designation (required, unique), 
    IAU name (optional), diameter in kilometers (optional - sometimes unknown), and whether it's marked as potentially hazardous to Earth.
        A `NearEarthObject` also maintains a collection of its close approaches - initialized to an empty collection, but eventually populated in
    the `NEODatabase` constructor.
    """
    # pdes - the primary designation of the NEO. This is a unique identifier in the database, and its "name" to computer systems.
    # name - the International Astronomical Union (IAU) name of the NEO. This is its "name" to humans.
    # pha - whether NASA has marked the NEO as a "Potentially Hazardous Asteroid," roughly meaning that it's large and can come quite close to Earth.
    # diameter - the NEO's diameter (from an equivalent sphere) in kilometers.

    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation, name=None, diameter=float('nan'), hazardous=False, **info):     # (self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        self.designation = str(designation) #### => required!
        self.name = str(name)   #### should I use an IF couse here??? If I use str(name) the None value will be converted to a string
        if name == '':
            self.name = None
        else:
            self.name = str(name)
        if diameter == '':
            self.diameter = float('nan')
        else:
            self.diameter = float(diameter)
        if hazardous == 'Y':
            self.hazardous = True
        elif hazardous == 'N':  # ? this may not be necessary because the default value for "hazardous" is False
            self.hazardous = False
        else:
            self.hazardous = False #'Hazardous ERROR!!' # ? If I omit this line the code doesn't work, but is it OK to set hazardous to False if there is not value present in the neo object? 
        # self.hazardous = bool(hazardous) #### => required? => I'm not sure if I need to set the defauilt value to False
        self.info = info 

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        # TODO: Use self.designation and self.name to build a fullname for this object.
        if self.name == None:
            return f'{self.designation}'
        else:
            return f'{self.designation} ({self.name})'

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        # examples:
        # NEO {fullname} has a diameter of {diameter:.3f} km and [is/is not] potentially hazardous.
        # >>> print(halley)
        # NEO 433 (Eros) has a diameter of 16.840 km and is not potentially hazardous.
        is_hazardous = ''
        if self.hazardous == True:
            is_hazardous = 'is'
        else:
            is_hazardous = 'is not'
        has_diameter = ''
        if self.diameter != float('nan'):
            has_diameter = f'has a diameter of {self.diameter:.3f} km and'
        return f"NEO {self.fullname} {has_diameter} {is_hazardous} potencially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
            f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # des - primary designation of the asteroid or comet (e.g., 443, 2000 SG344) 
    # cd - time of close-approach (formatted calendar date/time, in UTC) 
    # dist - nominal approach distance (au) 
    # v_rel - velocity relative to the approach body at close approach (km/s) 

    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation, time, distance, velocity, **neo): #, **info): # TODO: check if I really need "**neo" because I'll pass an object, so I may pass just "neo"
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        self._designation = str(designation)  #''  "des" field
        self.time = cd_to_datetime(time)    # None  "cd" field # TODO: Use the cd_to_datetime function for this attribute.
        self.distance = float("{:.2f}".format(float(distance))) # "dist" field # TODO: verify if I really need the first "float" because I'm already passing a float in the ".format(float(distance))"
        # ! the first float is REALLY necessary because without it I would have a string and not a float!
        self.velocity = float("{:.2f}".format(float(velocity))) # "v_rel" field # TODO: same as the above

        # Create an attribute for the referenced NEO, originally None.
        # ? perhaps I'm having problems because of this statement in Task 1:
        # ? The neo attribute, for now, can be None. In its absence, you should include a _designation attribute with the 
        # ? primary designation of the close approach's NEO. 
        # ? In Task 2, you'll use the real data set and this _designation attribute to connect the neo attribute to a real NearEarthObject instance.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # TODO: Use this object's `.time` attribute and the `datetime_to_str` function to
        # build a formatted representation of the approach time.
        approach_time = datetime_to_str(self.time)
        return approach_time
        # TODO: Use self.designation and self.name to build a fullname for this object.
        # return ''

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return f"On {self.time_str}, {self._designation} approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."
    #### I must change self._designation to neo.fullname!

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
            f"velocity={self.velocity:.2f}, neo={self.neo!r})"
