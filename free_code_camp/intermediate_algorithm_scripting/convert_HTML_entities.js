function convertHTML(str) {
  let arr = str.split('');
  console.log(arr);
  arr = arr.map(convertChar);
  console.log(arr.join(''));
  return arr.join('');
}

function convertChar(char) {
    switch (char) {
      case '&':
        return '&amp;'
      case '<':
        return '&lt;'
      case '>':
        return '&gt;'
      case '"':
        return '&quot;'
      case "'":
        return '&apos;'
      default:
        return char
    }
  }
