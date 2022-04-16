# Class: CoordTf
# Contents: Frequently used geodetic transformations
# Functions: cart2ellip, ellip2cart, cart2sph, sph2cart
# Author: Simran Suresh
# Date: 15.04.2022

# TODO: geodetic2enu test again, add more transformations if necessary

import numpy as np
from constants import WGS84, GRS80, Constants


class CoordTf:
    def __init__(self):
        pass

    def cart2ellip(self, x, y, z, ref=None):
        """
        SRC: https://gssc.esa.int/navipedia/index.php/Ellipsoidal_and_Cartesian_Coordinates_Conversion
        transformation of cartesian to ellipsoidal or llh coordinates or ECEF coordinates
        x: x coordinate/easting
        y: y coordinate/northing
        z: height 
        ref: WGS84 or GRS80. Default will be WGS84
        returns: x,y,z
        """
        # set reference system
        ref = GRS80() if ref == "GRS80" else WGS84()

        # ellipsoidal longitude
        lon = np.arctan(y / x)

        # ellipsoidal latitude, h computation needs iteration as h needs lat and lat needs h too
        # init
        p = np.sqrt(x**2 + y**2)
        h0 = 0
        lat0 = np.arctan(z / (1 - ref.e2)*p)
        epsilon = 0.1e-3
        iter = True

        # iteration
        while iter:
            # radius of curvature changes wrt lat
            N = ref.a / np.sqrt(1 - ref.e2*np.sin(lat0)**2)
            h = p / np.cos(lat0) - N
            lat = np.arctan((z / p) / (1 - ref.e2* N / (N+h)))

            if abs(h-h0) < epsilon and Constants().R * abs(lat-lat0) < epsilon:
                iter = False

            h0 = h
            lat0 = lat

        return np.rad2deg(lat), np.rad2deg(lon), h


    def ellip2cart(self, lat, lon, h, ref=None):
        """
        SRC: https://gssc.esa.int/navipedia/index.php/Ellipsoidal_and_Cartesian_Coordinates_Conversion
        transformation of ellipsoidal or llh coordinates to cartesian 
        lat: latitude 
        lon: longitude
        h: ellipsoidal height
        ref: WGS84 or GRS80. Default will be WGS84
        returns: lat, lon, h
        """
        # set reference system
        ref = GRS80() if ref == "GRS80" else WGS84()

        # np sin, cos accept in radian format only
        lat, lon = np.deg2rad(lat), np.deg2rad(lon)

        # radius of curvature
        N = ref.a / (1 - ref.e2*np.sin(lat)**2)

        # cartesian coordinates
        x = (N + h) * np.cos(lat) * np.cos(lon)
        y = (N + h) * np.cos(lat) * np.sin(lon)
        z = ((1 - ref.e2)*N + h) * np.sin(lat)

        return x, y, z


    def cart2sph(self, x, y, z):
        """
        SRC: https://en.wikipedia.org/wiki/Spherical_coordinate_system
        transformation of cartesian to spherical coordinates
        x,y,z: Cartesian coordinates
        returns: r, inclination, azimuth
        """
        # radius
        r = np.sqrt(x**2 + y**2 + z**2)

        # inclination theta
        theta = np.arctan(np.sqrt(x**2 + y**2) / z)

        # azimuth angle phi
        phi = np.arctan(y / x)

        return r, np.rad2deg(theta), np.rad2deg(phi)


    def sph2cart(self, r, theta, phi):
        """
        SRC: https://en.wikipedia.org/wiki/Spherical_coordinate_system
        transformation of spherical to cartesian coordinates
        r, inclination, azimuth: spherical coordinates
        returns: x, y, z
        """
        # np sin, cos accept in radian format only
        theta, phi = np.deg2rad(theta), np.deg2rad(phi)

        # cartesian coordinates
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)

        return x, y, z


    def geodetic2enu(self, lat, lon, h):
        """
        SRC: https://gssc.esa.int/navipedia/index.php/Transformations_between_ECEF_and_ENU_coordinates
        transformation of Earth centered earth fixed frame to Easting Northing Up coordinates
        lat, lon, h: geodetic coordinates
        returns E,N,U
        """
        # convert geodetic coordinates to cartesian ECEF
        x, y, z = self.ellip2cart(lat, lon, h)

        # center is not given, consider greenwich meridien
        center = np.array([51.4780, 0.0015, 0])
        dcenter = (np.array([x, y, z]).T - center).T

        # EQN:6 R1(pi/2 - lat)*R3(pi/2 + lon)
        rot_mat = np.array([
            [-np.sin(lon), np.cos(lon), 0],
            [-np.cos(lon)*np.sin(lat), -np.sin(lon)*np.sin(lat), np.cos(lat)],
            [np.cos(lon)*np.cos(lat), np.sin(lon)*np.cos(lat), np.sin(lat)]
        ])

        # ENU coordinates
        E, N, U = rot_mat @ dcenter

        return E, N, U
        