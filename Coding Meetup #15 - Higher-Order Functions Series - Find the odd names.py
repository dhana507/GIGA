function findOddNames(list) {
  // thank you for checking out the Coding Meetup kata :)
  return list.filter((developer) => {
    const firstNameAsciiSum = developer.firstName.split('').reduce((sum, char) => sum + char.charCodeAt(0), 0);
    return firstNameAsciiSum % 2 !== 0;
  });
}
