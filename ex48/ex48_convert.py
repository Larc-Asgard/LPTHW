def covert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
