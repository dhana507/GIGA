def is_ruby_coming(lst): 
    # your code here
    flag=False
    for i in lst:
        if(i['language']=='Ruby'):
            flag=True
    return flag
