def get_first_python(users):
    pass
    for i in users:
        if(i['language']=='Python'):
            return i['first_name']+', '+i['country']
    else:
        return "There will be no Python developers"
