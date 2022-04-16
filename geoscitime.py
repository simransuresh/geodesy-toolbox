# Class: GeoSciTime
# Contents: Time systems used in geoscientific programming
# Functions: date2mjd, mjd2date, date2toy, toy2date, others date parse already captured by strptime ..
# Author: Simran Suresh
# Date: 16.04.2022


import math


class GeoSciTime:
    def __init__(self):
        pass

    def mjd2jd(self, mjd):
        """
        converts mjd to jd
        mjd: modified julian date
        returns: jd
        """
        return mjd + 2400000.5


    def jd2mjd(self, jd):
        """
        converts jd to mjd
        jd: julian date
        returns: mjd
        """
        return jd - 2400000.5


    def date2mjd(self, year, month, day):
        """
        SRC: Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet', 
        4th ed., Duffet-Smith and Zwart, 2011.
        year, month, day: date in format yyyy, mm, dd 
        returns: modified julian date mjd
        """
        if month == 1 or month == 2:
            yearp = year - 1
            monthp = month + 12
        else:
            yearp = year
            monthp = month
    
        # beginning of the Gregorian calendar check.
        if ((year < 1582) or
            (year == 1582 and month < 10) or
            (year == 1582 and month == 10 and day < 15)):
            # before start
            B = 0
        else:
            # after start
            A = math.trunc(yearp / 100.)
            B = 2 - A + math.trunc(A / 4.)
            
        if yearp < 0:
            C = math.trunc((365.25 * yearp) - 0.75)
        else:
            C = math.trunc(365.25 * yearp)
            
        D = math.trunc(30.6001 * (monthp + 1))
        
        jd = B + C + D + day + 1720994.5
        
        return self.jd2mjd(jd)


    def mjd2date(self, mjd):
        """
        SRC: Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet', 
        4th ed., Duffet-Smith and Zwart, 2011.
        mjd: modified julian date
        returns: tuple of year, month, day
        """
        jd = self.mjd2jd(mjd)

        jd = jd + 0.5
    
        F, I = math.modf(jd)
        I = int(I)
        
        A = math.trunc((I - 1867216.25)/36524.25)
        
        if I > 2299160:
            B = I + 1 + A - math.trunc(A / 4.)
        else:
            B = I
            
        C = B + 1524
        
        D = math.trunc((C - 122.1) / 365.25)
        
        E = math.trunc(365.25 * D)
        
        G = math.trunc((C - E) / 30.6001)
        
        day = C - E + F - math.trunc(30.6001 * G)
        
        if G < 13.5:
            month = G - 1
        else:
            month = G - 13
            
        if month > 2.5:
            year = D - 4716
        else:
            year = D - 4715
            
        return year, month, day


    def date2percent(self, year, month, day):
        """
        convert date to percent of the year
        eg: 2022, 5, 12 => 2022.3616438356164 and 2020, 1, 12 => 2020.032786885246
        args: year, month, day
        returns: year.percent
        """
        days_num = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        
        # leap year check
        if year % 4 == 0:
            days_num[2] = 29

        # for first month, days elapsed is number of days
        if month == 1:
            days_elapsed = day
        else:
        # for remaining months, it is total number of days till previous month and days in current month
            days_elapsed = sum([val for key, val in days_num.items() if key < month]) + day

        # percent of the year
        return days_elapsed/sum(days_num.values()) + year
