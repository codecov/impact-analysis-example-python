from datetime import datetime

def format_time(time):
    return datetime.strftime(time, '%Y-%m-%d%H:%M:%S')
