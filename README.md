# geodesy-toolbox
A complete handy toolbox for geodesy in Python

# Agenda
Foundations:
1. Coordinate transformations: cart2sph, sph2cart, cart2ellip, ellip2cart
2. Earth constants, Datum/RF specifications - wgs84 datum a,f, grs80 ellipsoid constants
3. Time systems: date2mjd, mjd2date, doy, gpst, sidereal day, year, essential constants

Earth Rotations: (PILLAR 1)
4. ITRF-ICRF, ICRF-ITRF transformation - EOP

Celestial mechanics: (DESIGN OF SATELLITE MISSION/ORBIT PLANNING)
5. Satellite orbits, keplerian elements, pertubations, osculating orbit
6. geostationary, geosynchronous, polar repeat orbit conditions, altitude-inclination-repeat period design

Gravity: (PILLAR 2)
7. gravity functionals - GH, GD, GA
8. Spherical harmonics analysis and synthesis

Shape and Size of Earth: (PILLAR 3)
9. Sea surface functions - SSH, SSL, SSA, MDT

Utils:
10. Signal synthesizer, correlator, convolution operator, Noise generator, echo waveform analyser
11. Corrections: cloud removal, ocean tides, atmospheric tides, luni-solar tides, loading ...
12. Filters: KF, EKF, EnKF, PF, Collocation
13. Least squares adjustment, Regressor, Smoother, Interpolator
