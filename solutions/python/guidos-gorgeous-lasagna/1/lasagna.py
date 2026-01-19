
EXPECTED_BAKE_TIME = 40
 
def bake_time_remaining(time):
    """returns the remaining time"""
    return EXPECTED_BAKE_TIME - time

def preparation_time_in_minutes(NL):
    """returns with 2 minutes for each layer"""
    return NL * 2

def elapsed_time_in_minutes(time, NL):
    """total time"""
    tot = preparation_time_in_minutes(time) + NL
    return tot


    