# Contents: transformation of ICRF to ITRF and vice-versa
# Functions: icrf2itrf, itrf2icrf, precession, nutation, earth_rotation, polar_motion
# Author: Simran Suresh
# Date: 16.04.2022
# SRC: https://gssc.esa.int/navipedia/index.php/ICRF_to_CEP, 
# https://gssc.esa.int/navipedia/index.php/CEP_to_ITRF

# TODO: Nutation model latest import, nutation matrix, Earth rotation, polar motion matrix, TF


from rot_mat import *
from geoscitime import date2mjd, mjd2jd

def precession(year, month, day):
    """
    defines precession matrix
    Precession is the long term wobbling of rotation axis wrt mean. Period: 25772 years [SRC: Google]
    args:
    returns:
    """
    mjd = date2mjd(year, month, day)
    jd = mjd2jd(mjd)

    # julian century
    T = jd - 2451545.0 / 36525

    z = 2306.2181 * T + 1.09468 * T**2 + 0.018203 * T**3
    v = 2004.3109 * T - 0.42665 * T**2 - 0.041833 * T**3 
    c = 2306.2181 * T + 0.30188 * T**2 + 0.017998 * T**3

    return Rz(-z) * Ry(v) * Rz(-c)

# def nutation(year, month, day):
    
     


