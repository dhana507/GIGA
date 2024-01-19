def find_admin(lst, lang): 
    # your code here
    d=[]
    for i in lst:
        if(i['language']==lang and  i['githubAdmin']=='yes'):
            d.append(i)
    return d
