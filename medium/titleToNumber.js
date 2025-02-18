function titleToNumber(title) {
  let sum = 0;
  let base = 0;
  for (let i = title.length - 1; i >= 0; i--) {
    const value = title.charCodeAt(i) - 64;
    const exp = 26 ** base;
    const total = exp * value;
    sum += total;
    base++;
  }
  return sum;
}
