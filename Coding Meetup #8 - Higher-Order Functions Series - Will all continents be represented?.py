def all_continents(lst): 
    # your code here
    a=False
    b=False
    c=False
    d=False
    e=False
    for i in lst:
        if(i['continent']=='Africa'):
            a=True
        elif(i['continent']=='Americas'):
            b=True
        elif(i['continent']=='Asia'):
            c=True
        elif(i['continent']=='Europe'):
            d=True
        elif(i['continent']=='Oceania'):
            e=True
    if(a and b and c and d and e):
        return True
    else:
        return False
        
