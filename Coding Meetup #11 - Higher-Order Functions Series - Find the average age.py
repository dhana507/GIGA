function getAverageAge(list) {
  // thank you for checking out the Coding Meetup kata :)
  const totalAge = list.reduce((sum, developer) => sum + developer.age, 0);

  // Calculate the average age
  const averageAge = Math.round(totalAge / list.length);

  return averageAge;
}
