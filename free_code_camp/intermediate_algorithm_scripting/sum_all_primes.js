function sumPrimes(num) {
  let no_prime = []
  let sum = 0;
  for(let i = 0; i <= num; i++){
    if(no_prime.indexOf(i) === -1 && i!== 0 && i !== 1){
      sum += i
      for(let j=i; j <= num; j+=i){
        no_prime.push(j)
      }
    }
  }
  return sum;
}

sumPrimes(10);
