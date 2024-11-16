#!/usr/bin/env python3
# Student ID: ekoleci
class Time:
    """Simple object type for time of the day."""

    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        '''Return a string representation for the object self.'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        '''Return a detailed string representation for interactive shells.'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def sum_times(self, t2):
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def time_to_sec(self):
        '''Convert a time object to total seconds.'''
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

def sec_to_time(seconds):
    '''Convert a given number of seconds to a time object.'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
