import datetime
import re
from collections import defaultdict
from typing import List


class Shift:
    def __init__(self):
        self.date: datetime.datetime = None
        self.guard_id: int = None
        self.guard_status: bool = None
        self.is_first: bool = False

    def __repr__(self):
        return f"[{self.date}] {self.guard_id} {self.guard_status}"


def solve_a(input_file_lines: List[str]) -> str:
    shifts = []
    for line in input_file_lines:
        shift = Shift()
        date, rest = re.fullmatch("\[(\d+-\d+-\d+ \d+:\d+)\] \w+ (.*?)[ .*]?", line).groups()
        date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
        shift.date = date
        if rest[0] == "#":
            shift.is_first = True
            shift.guard_id = int(re.fullmatch("#(\d+).*", rest)[1])
        else:
            shift.is_first = False
            shift.guard_status = True if rest == "up" else False
        shifts.append(shift)
    shifts.sort(key=lambda sh: sh.date)
    guard_id = None
    sleep_totals = defaultdict(lambda: [0 for _ in range(60)])
    last_sleep_time = None
    for shift in shifts:
        if shift.is_first:
            guard_id = shift.guard_id
            last_sleep_time = None
        else:
            if not shift.guard_status:
                assert last_sleep_time is None
                last_sleep_time = shift.date
            else:
                assert last_sleep_time is not None
                time_asleep = shift.date - last_sleep_time
                minutes_asleep = int(time_asleep.total_seconds()/60)
                for i in range(last_sleep_time.minute, last_sleep_time.minute + minutes_asleep):
                    sleep_totals[guard_id][i % 60] += 1
                last_sleep_time = None
    most_sleep = -1
    most_asleep_guard_id = None
    sleepiest_minute = None
    for guard_id in dict(sleep_totals):
        hours_asleep = sum(sleep_totals[guard_id])
        if most_sleep < hours_asleep:
            most_sleep = hours_asleep
            most_asleep_guard_id = guard_id
            sleepiest_minute_value = max(sleep_totals[guard_id])
            for minute in range(60):
                if sleep_totals[guard_id][minute] == sleepiest_minute_value:
                    sleepiest_minute = minute
    return str(most_asleep_guard_id * sleepiest_minute)


def solve_b(input_file_lines: List[str]) -> str:
    shifts = []
    for line in input_file_lines:
        shift = Shift()
        date, rest = re.fullmatch("\[(\d+-\d+-\d+ \d+:\d+)\] \w+ (.*?)[ .*]?", line).groups()
        date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
        shift.date = date
        if rest[0] == "#":
            shift.is_first = True
            shift.guard_id = int(re.fullmatch("#(\d+).*", rest)[1])
        else:
            shift.is_first = False
            shift.guard_status = True if rest == "up" else False
        shifts.append(shift)
    shifts.sort(key=lambda sh: sh.date)
    guard_id = None
    sleep_totals = defaultdict(lambda: [0 for _ in range(60)])
    last_sleep_time = None
    for shift in shifts:
        if shift.is_first:
            guard_id = shift.guard_id
            last_sleep_time = None
        else:
            if not shift.guard_status:
                assert last_sleep_time is None
                last_sleep_time = shift.date
            else:
                assert last_sleep_time is not None
                time_asleep = shift.date - last_sleep_time
                minutes_asleep = int(time_asleep.total_seconds()/60)
                for i in range(last_sleep_time.minute, last_sleep_time.minute + minutes_asleep):
                    sleep_totals[guard_id][i % 60] += 1
                last_sleep_time = None
    most_who_slept_each_minute = defaultdict(lambda: (-1, 0))
    for guard_id in dict(sleep_totals):
        for minute in range(60):
            if sleep_totals[guard_id][minute] > most_who_slept_each_minute[minute][1]:
                most_who_slept_each_minute[minute] = (guard_id, sleep_totals[guard_id][minute])
    most_asleep_guard_id = None
    sleepiest_minute = None
    sleepiest_minute_amount = -1
    for minute in range(60):
        guard_id, amount = most_who_slept_each_minute[minute]
        if sleepiest_minute_amount < amount:
            sleepiest_minute_amount = amount
            sleepiest_minute = minute
            most_asleep_guard_id = guard_id

    return str(most_asleep_guard_id * sleepiest_minute)

