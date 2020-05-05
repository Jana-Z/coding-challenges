function convertToRoman(num) {
  const roman = [['I', 'V'], ['X', 'L'], ['C', 'D'], ['M']];
  let arr = Array.from(String(num), Number).reverse();
  let res = ''
  for (let i = 0; i < arr.length; i++){
    console.log(arr[i])
    switch (arr[i]){
      case 1:
        res += roman[i][0]
        break
      case 2:
        res += roman[i][0].repeat(2)
        break
      case 3:
        res += roman[i][0].repeat(3)
        break
      case 4:
        res += roman[i][1] + roman[i][0]
        break
      case 5:
        res += roman[i][1]
        break
      case 6:
        res += roman[i][0] + roman[i][1]
        break
      case 7:
        res += roman[i][0].repeat(2) + roman[i][1]
        break
      case 8:
        res += roman[i][0].repeat(3) +  roman[i][1]
        break
      case 9:
        res += roman[i+1][0] + roman[i][0]
    }
  }
  return res.split('').reverse().join('');
}
