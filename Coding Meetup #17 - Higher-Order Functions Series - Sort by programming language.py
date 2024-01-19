function sortByLanguage(list) {
 
   list.sort((a, b) => {
  
    if (a.language !== b.language) {
      return a.language.localeCompare(b.language);
    }

    
    return a.firstName.localeCompare(b.firstName);
  });

  return list;
}
