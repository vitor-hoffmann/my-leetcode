function spinWords(input) {
  let splited = input.split(" ");

  for (let i = 0; i < splited.length; i++) {
    if (splited[i].length >= 5) {
      splited[i] = splited[i].split("").reverse().join("");
    }
  }
  return splited.join(" ");
}
