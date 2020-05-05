function binaryAgent(str) {
  let arr = str.split(' ');
  arr = arr.map(x => String.fromCharCode(parseInt(x, 2)))
  return arr.join('');
}
