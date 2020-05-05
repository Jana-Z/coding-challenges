function rot13(str) {
  let arr = str.split('')
  let alphabeth =  [ 'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z' ]
  for(let i=0; i < arr.length; i ++){
    if(alphabeth.indexOf(arr[i]) >= 0){
      arr[i] = alphabeth[(alphabeth.indexOf(arr[i])+13)%alphabeth.length]
    }
  }
  console.log(arr.join(''))
  return arr.join('');
}
