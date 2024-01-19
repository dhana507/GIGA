def order_food(lst): 
    # your code here
    food_count = {}
    
    for developer in lst:
        meal_option = developer['meal']
        food_count[meal_option] = food_count.get(meal_option, 0) + 1
    
    return food_count
