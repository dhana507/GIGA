function isLanguageDiverse(list) {
  // thank you for checking out the Coding Meetup kata :)
   const languageCount = {};
  
  // Count the occurrences of each programming language
  for (const developer of list) {
    const language = developer.language;
    languageCount[language] = (languageCount[language] || 0) + 1;
  }

  // Check if the number of developers for any language is more than 2 times the number of developers for any other language
  const languageCounts = Object.values(languageCount);
  const maxCount = Math.max(...languageCounts);
  const minCount = Math.min(...languageCounts);

  return maxCount <= 2 * minCount;
}
