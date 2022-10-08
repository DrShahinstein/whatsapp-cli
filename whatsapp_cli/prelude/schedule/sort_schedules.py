def sort_schedules(schedules):
    sorted_schedules = sorted(schedules, key=lambda schedule: int(
        schedule["hours"]) * 60 + int(schedule["minutes"]))
    return sorted_schedules
