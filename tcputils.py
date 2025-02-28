"""
TCPUtils
"""

import threading

StringIP = type("StringIP", (str,), {})

class TCP:
    def log(self, *info: str, level: int = 1, levelup: int = 0):
        """
        Log by print info

        Arguments:
            info -- Info to print
            level -- Log level

        Keyword Arguments:
            levelup -- The level adds to the original log level,
            -1 means force log output (default: {0})
        """
        if level + levelup >= self.log_level or levelup == -1:
            print(*info)

class LockedVar:
    def __init__(self, value):
        self._value = value
        self._lock = threading.Lock()
    
    def get(self):
        with self._lock:
            return self._value
