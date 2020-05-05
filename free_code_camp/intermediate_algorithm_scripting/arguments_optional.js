function addTogether() {
  let num1 = arguments[0];
  if (typeof(num1) !== "number"){
    return undefined;
  }
  if (arguments.length === 2){
    if (typeof(arguments[1]) !== "number"){
      return undefined;
    }
    return arguments[0] + arguments[1];
  }
  else{
    return function(x){
      if (typeof(x) !== "number"){
        return undefined
      }
      return num1 + x;
    }
  }
}
