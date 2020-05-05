function uniteUnique() {
  var unique = []
  for(let i = 0; i < arguments.length; i++){
    unique = unique.concat(arguments[i]);
    unique = unique.filter( onlyUnique );
  }
  console.log(unique)
  return unique
}

function onlyUnique(value, index, self) { 
    return self.indexOf(value) === index;
}

uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]);
