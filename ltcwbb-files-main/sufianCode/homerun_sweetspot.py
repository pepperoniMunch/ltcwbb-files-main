def hr_sweetspot(launch_angle, exit_velocity):
    """
    the function takes launch angle and exit velocity into account, outputting a
    boolean describing whether the ball was hit in a "homerun sweetspot"
    """
    return (25 <= launch_angle <= 35) and (exit_velocity >= 95)

def noisy_hr_sweetspot(launch_angle, exit_velocity)
    """
    the function takes launch angle and exit velocity into account, outputting a
    boolean describing whether the ball was hit in a "homerun sweetspot" - function
    also prints out the launch angle
    """
    print(launch_angle)
    return (25 <= launch_angle <=35) and (exit_velocity >=95)

def hr_sweetspot_wdefault(launch_angle = 14, exit_velocity = 68):
    """
    describe function
    """
    return (25 <= launch_angle <= 35) and (exit_velocity >= 95)

# Functions can take other functions
def do_to_list(working_list, working_fn, desc):
    """
    this function takes a list, a function, and a description
    it applies a function a list, then prints out a description and value
    """
    value = working_fn(working_list)
    return f'{desc}, {value}'

# Create working_fn
def last_elem_in_list(working_list):
    """
    returns the last element in a list
    """
    return working_list[-1]

infield = ['1B', '2B', '3B', 'P', 'C', 'SS']

do_to_list(infield, last_elem_in_list)
