function dropElements(arr, func) {
  for(let i = 0; i < arr.length; i++){
    if (func(arr[i])){
      console.log(arr)
      return arr
    }
    else{
      arr.shift()
      i --
    }
  }
  return arr;
}
