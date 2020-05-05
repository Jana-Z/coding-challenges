function sumFibs(num) {
  let fib1 = 0;
  let fib2 = 1;
  let sum = 0;
  for(let i = 0; fib2 <= num; i++){
    if (fib2%2 === 1){
      sum += fib2;
    }
    let help = fib1;
    fib1 = fib2;
    fib2 = fib1 + help;
  }
  return sum
}

sumFibs(1);
