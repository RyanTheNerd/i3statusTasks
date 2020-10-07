#!/usr/bin/env python3

from datetime import date
import json
import sys

class Task:
    def __init__(self, taskName, start, freq=1, time=0, offsetDays=0):
        self.taskName = taskName
        self.start = date(*start)
        self.freq = freq
        self.time = f"{time} minutes"
        self.offsetDays = offsetDays
        self.daysSince = -1
        self.timeText = f"{time} minutes" if time > 0 else None

    def getJSON(self, completed = False):

        daysSince = (date.today() - self.start).days

        if self.daysSince == daysSince:
            return self.lastUpdate

        else:
            if self.freq == 1:
                pass 
            elif((daysSince + self.offsetDays) % self.freq) == False:
                return None
            
            if(completed == False):
                color = "#ff0000"
            else: 
                color = "#00ff00"
            
            statusText = "Complete" if completed else "Incomplete"
            taskText = f"{self.taskName}: day {daysSince} ({statusText})"

            self.lastUpdate = {
                "full_text": f"{taskText}",
                "color": color
            }
            return self.lastUpdate 

tasks = [
    Task("Exercise", [2020, 10, 2], freq=2, offsetDays=1),
    Task("Code", [2020, 10, 2]),
    Task("Job searching", [2020, 10, 2], freq=2)
]


def print_line(message):
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()

def read_line():
    """ Interrupted respecting reader for stdin. """
    # try reading a line, removing any extra whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    # Skip the first line which contains the version header.
    print_line(read_line())

    # The second line contains the start of the infinite array.
    print_line(read_line())

    while True:
        line, prefix = read_line(), ''
        # ignore comma at start of lines
        if line.startswith(','):
            line, prefix = line[1:], ','

        j = json.loads(line)
        # insert information into the start of the json, but could be anywhere
        # CHANGE THIS LINE TO INSERT SOMETHING ELSE
        for task in tasks:
            j.insert(0, task.getJSON())
        # and echo back new encoded json
        print_line(prefix+json.dumps(j))

