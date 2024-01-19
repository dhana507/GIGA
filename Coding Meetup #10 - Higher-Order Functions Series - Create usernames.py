function addUsername(list) {
  // thank you for checking out the Coding Meetup kata :)
 const currentYear = new Date().getFullYear();

  return list.map((developer) => {
    const birthYear = currentYear - developer.age;
    const username = `${developer.firstName.toLowerCase()}${developer.lastName[0].toLowerCase()}${birthYear}`;
    
    return { ...developer, username };
  });
}
