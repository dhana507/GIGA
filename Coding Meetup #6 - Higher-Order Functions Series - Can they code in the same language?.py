def is_same_language(lst): 
    # your code here
    language=lst[0]['language']
    c=0
    for i in lst:
        if(i['language']==language):
            c+=1
    if(c==len(lst)):
        return True
    else:
        return False
