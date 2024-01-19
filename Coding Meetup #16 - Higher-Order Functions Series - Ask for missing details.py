function askForMissingDetails(list) {
  // thank you for checking out the Coding Meetup kata :)
  const missingDetailsDevelopers = [];

  for (const developer of list) {
    const missingProperties = Object.entries(developer)
      .filter(([key, value]) => value === null)
      .map(([key]) => key);

    if (missingProperties.length > 0) {
      const question = `Hi, could you please provide your ${missingProperties.join(', ')}.`;
      missingDetailsDevelopers.push({ ...developer, question });
    }
  }

  return missingDetailsDevelopers;
}
