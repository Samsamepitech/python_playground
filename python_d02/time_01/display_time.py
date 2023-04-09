import time
from datetime import datetime
import calendar

def display_time(t):
    
    print(time.strftime("%H:%M:%S, %A, %w * day of the %V *week of %Y, %B", time.gmtime(t)))

