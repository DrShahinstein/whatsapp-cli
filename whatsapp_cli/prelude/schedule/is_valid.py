def is_valid_time(hours, minutes):
    if hours.isnumeric() and minutes.isnumeric():
        if int(hours) * 3600 + int(minutes) * 60 <= 86400:
            return True
    return False
