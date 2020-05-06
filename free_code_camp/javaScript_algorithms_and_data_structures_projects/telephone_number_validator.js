function telephoneCheck(str) {
  if ( /[\?]/.test(str)){
    return false
  }
  str = str.replace(/\s/g, '')  // White spaces dont matter
  let digits = str.replace(/\D/g, '')
  console.log(digits, str, digits.length, /[\?]/.test(str))
  // telephone number too long or too short
  if (digits.length < 10 || digits.length > 11){
    return false
  }
  // country code
  if (digits.length === 11){
    if(!(digits.startsWith("1"))){
      return false
    }
    else{
        str = str.slice(1, str.length)
        digits = str.replace(/\D/g, '')
    }
  }
  // just digits
  if (str === digits && str.length === 10){
    return true
  }
  if ((str.indexOf('(') === str.indexOf(')')) && str.indexOf('(') === -1){
    return true
  }
  else{
    return ((4 === str.indexOf(')')) && (str.indexOf('(') === 0))
  }
}
