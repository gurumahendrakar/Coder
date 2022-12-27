from datetime import date,time,datetime,timedelta,timezone
import pytz

# --------------------------------------Datetime-----------------------------------------------------------

datetime1 = datetime(year=2022,month=6,hour=2,minute=33,second=33,day=3,tzinfo = pytz.UTC) # Isko Arguments Dena Zarori Hai
# 2022-06-03 02:33:33 -> Datetime returned

# print('day : ',datetime1.day)
# print('month : ',datetime1.month)
# print('year : ',datetime1.year)
# print('hour : ',datetime1.hour)
# print('minute : ',datetime1.minute)
# print('second : ',datetime1.second)
# print('microsecond : ',datetime1.microsecond)
#
# print()
# print()
#
# print("\t -------datetime.today()-------")


#----------------today-------------------

datetime2 = datetime.today() # Hume Current Time Batata Hai
# 2022-11-25 00:33:56.503419
#
# print('day -- ',datetime2.day)
# print('month -- ',datetime2.month)
# print('year -- ',datetime2.year)
# print('hour -- ',datetime2.hour)
# print('minute -- ',datetime2.minute)
# print('second -- ',datetime2.second)
# print('microsecond -- ',datetime2.microsecond)
#
#
# print(datetime.fromisocalendar(2022,3,4)) # returned  : 2022-01-20 00:00:00
# print(datetime.fromisoformat('2011-11-04')) # returned : 2011-11-04 00:00:00
#
#
# #-------------------Ctime-------------------
# print('C-time',datetime.ctime(datetime1))
#

#------------------asctimezone---------------

# asctime = ('Asctimezone :',datetime1.astimezone())
# datetimenow = datetime.now()
# for timezones in pytz.all_timezones:
#     print(timezones,datetimenow.astimezone(pytz.timezone(timezones)))
#---------------------------------------------------------date----------------------------------------------------------
#
# date = date(2022,3,3)
# print(date.isoweekday()) # 1 Sunday to Monday
# print(date.weekday()) # 0 Sunday to Monday
# print(date.ctime())
# print(date.isoformat()) # returned -> 2022-03-03
# print(date.month)
# print(date.day)
# print(date.year)
#
#

#---------------------------------------------------------time----------------------------------------------------
<<<<<<< HEAD

=======
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418
# time = time(hour=3 ,minute=44,second=22,microsecond=222)
# print('minute :' ,time.minute)
# print(time.max) # hour many hours seconds minutes in day  : 23:59:59.999999
# print(time.min) # 00:00:00
#

# ----------------------------------------------------timedelta------------------------------------------------------

#
# timedelta = timedelta(days=33,hours=2)
# print(datetime1)
#
# print('days incresed',timedelta+datetime1) # timedelta me arguments pass karoge to jo pass karoge - + new object create karega aur timedetla me jo values daali hai
# # Osse o increse karega
#
# print('days decresed',datetime1  - timedelta)
# print(timedelta.total_seconds())
# print(timedelta.min)
# print(timedelta.days)
# print(timedelta.seconds)
<<<<<<< HEAD

=======
#
#
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418

# ---------------------------------------------------strftime-------------------------------------------------------------
#
# %a - abbreviated weekday name
# %A - full weekday name
# %b - abbreviated month name
# %B - full month name
# %c - preferred date and time representation
# %C - century number (the year divided by 100, range 00 to 99)
# %d - day of the month (01 to 31)
# %D - same as %m/%d/%y
# %e - day of the month (1 to 31)
# %g - like %G, but without the century
# %G - 4-digit year corresponding to the ISO week number (see %V).
# %h - same as %b
# %H - hour, using a 24-hour clock (00 to 23)
# %I - hour, using a 12-hour clock (01 to 12)
# %j - day of the year (001 to 366)
# %m - month (01 to 12)
# %M - minute
# %n - newline character
# %p - either am or pm according to the given time value
# %r - time in a.m. and p.m. notation
# %R - time in 24 hour notation
# %S - second
# %t - tab character
# %T - current time, equal to %H:%M:%S
# %u - weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday=1
# %U - week number of the current year, starting with the first Sunday as the first day of the first week
# %V - The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week
# %W - week number of the current year, starting with the first Monday as the first day of the first week
# %w - day of the week as a decimal, Sunday=0
# %x - preferred date representation without the time
# %X - preferred time representation without the date
# %y - year without a century (range 00 to 99)
# %Y - year including the century
# %Z or %z - time zone or name or abbreviation
# %% - a literal % character
#

datetimenow = datetime.now()

print(datetimenow.strftime('%c'))
print(datetimenow.strftime('%a %j %m'))


