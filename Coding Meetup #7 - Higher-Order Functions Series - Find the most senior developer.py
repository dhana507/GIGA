def find_senior(lst): 
    # your code here
    max_age = max(dev['age'] for dev in lst)
    oldest_developers = [dev for dev in lst if dev['age'] == max_age]
    return oldest_developers
