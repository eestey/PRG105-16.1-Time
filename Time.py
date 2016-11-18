class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second
    """


time = Time()
time.hour = 3
time.minute = 10
time.second = 45

print('{0:0>2d}'.format(time.hour) + ':' + '{0:0>2d}'.format(time.minute) + ':' + '{0:0>2d}'.format(time.second))
