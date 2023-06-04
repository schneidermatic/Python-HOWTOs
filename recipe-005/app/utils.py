import functools
import time
from datetime import datetime, timezone

class Timer:
    def set_start_time(self):
        self.start_time = time.perf_counter()

    def get_run_time(self):
        return time.perf_counter() - self.start_time

class TimeStamp:
    @staticmethod
    def format():
        dt = datetime.utcnow()
        return "{}.{:03d}Z".format(dt.strftime('%Y-%m-%dT%H:%M:%S'), dt.microsecond//1000)
