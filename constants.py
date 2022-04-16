# Class: Constants
# Contents: Earth constants, Geodetic reference system constants
# Functions: 
# Author: Simran Suresh
# Date: 15.04.2022


class Constants:
    def __init__(self):
        # SRC: from Wiki

        # mass of earth [kg]
        self.M = 5.9722 * 10e24

        # gravitational constant [m3/kg*s2] defined in Newton's law of gravitation
        self.G = 6.674 * 10e-11

        # acceleration due to gravity [m/s2]
        self.g = 9.8067

        # radius of the earth rounded [km]
        self.R = 6371


class Reference_Systems:
    # https://de.wikipedia.org/wiki/World_Geodetic_System_1984

    def __init__(self):

        # semi major axis or equatorial radius [m]
        self.a = 6378137

        # geocentric gravitational constant = gravitational constant * earth mass [m3/s2]
        self.GM = 3.986004418 * 10**14

        # rotational speed of earth or angular velocity omega_e [rad/s]
        self.omega_e = 7.292115 * 10**-5

        # derived constants
        # semi minor axis b = a(1-f) = 6356752 [m]
        self.b = self.a * (1 - self.f)

        # eccentricity e owing to the bent of the ellipse
        # first eccentricity e2 = 1 - b2/a2 = 2f - f2
        self.e2 = 1 - self.b**2 / self.a**2

        # second eccentricity e′2 = a2/b2 - 1 = f(2-f)/(1-f)2
        self.e2_ = self.a**2 / self.b**2 - 1


class WGS84(Reference_Systems):
    # World Geodetic System 1984 (WGS84) is the best fit global datum
    # https://gssc.esa.int/navipedia/index.php/Reference_Frames_in_GNSS#GPS_reference_frame_WGS-84

    def __init__(self):

        # flattening of the earth
        self.f = 1 / 298257223563

        # super class constructor called here so that self.f is referenced 
        super().__init__()


class GRS80(Reference_Systems):
    # Geodetic Reference System 1980 (GRS80) reference system similar to WGS84
    # contains global reference ellipsoid and normal gravity model
    # https://en.wikipedia.org/wiki/Geodetic_Reference_System_1980

    def __init__(self):

        # flattening
        self.f = 1 / 298.257222100882711243

        # dynamic form factor J2
        self.j2 = 108263 * 10**-8

        super().__init__()

        