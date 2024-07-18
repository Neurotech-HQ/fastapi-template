# Define any enums here

from enum import Enum


class IDTypes(Enum):
    """
    The types of identification documents that can be used to verify a user's identity.
    """

    NATIONAL_ID = "national_id"
    PASSPORT = "passport"
    DRIVERS_LICENSE = "drivers_license"
