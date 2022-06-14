from datetime import datetime

from ..time import format_time

def test_time():
    current_time = datetime.now()
    assert(format_time(current_time) == datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S'))
