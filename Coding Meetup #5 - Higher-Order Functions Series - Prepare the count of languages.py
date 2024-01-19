def count_languages(lst): 
    # your code here
    language_count = {}  

    for i in lst:
        language = i['language']
        language_count[language] = language_count.get(language, 0) + 1

    return language_count
