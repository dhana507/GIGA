def is_age_diverse(lst): 
    # your code here
    age_groups = {
        'teens': range(13, 20),
        'twenties': range(20, 30),
        'thirties': range(30, 40),
        'forties': range(40, 50),
        'fifties': range(50, 60),
        'sixties': range(60, 70),
        'seventies': range(70, 80),
        'eighties': range(80, 90),
        'nineties': range(90, 100),
        'centenarian': range(100, 200),
    }

    for age_group, age_range in age_groups.items():
        if not any(dev['age'] in age_range for dev in lst):
            return False

    return True
