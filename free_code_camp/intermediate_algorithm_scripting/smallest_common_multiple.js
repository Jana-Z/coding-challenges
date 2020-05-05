function smallestCommons(arr) {
  let lower = Math.min(arr[0], arr[1])
  let higher = Math.max(arr[0], arr[1])
  let range = [...Array(higher - lower).keys()].map(i => i + lower)
  for (let i = lower; true; i++){
    let solution = true
    for (let num = lower; num <= higher; num++){
      if (i%num !== 0){
        solution = false
      }
    }
    if (solution){
      return i
    }
  }
}
