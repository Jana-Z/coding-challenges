function orbitalPeriod(arr) {
  var GM = 398600.4418;
  var earthRadius = 6367.4447;
  return arr.map(x => {
    return {'name': x['name'],
      'orbitalPeriod': Math.round(
        2*Math.PI
        *Math.sqrt(Math.pow(earthRadius + x['avgAlt'], 3) / GM)
      )}
  });
}
