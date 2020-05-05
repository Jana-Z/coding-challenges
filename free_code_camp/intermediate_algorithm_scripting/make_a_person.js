var Person = function(firstAndLast) {
  this.getFullName = function() {
    return firstAndLast;
  };
  this.getFirstName = function() {
    return firstAndLast.split(' ')[0];
  };
  this.getLastName = function(){
    return firstAndLast.split(' ')[1];
  };
  this.setFirstName = function(x) {
    firstAndLast = x + ' ' + firstAndLast.split(' ')[1];
  };
  this.setLastName = function(x) {
    firstAndLast = firstAndLast.split(' ')[0] + ' ' + x;
  };
  this.setFullName = function(x) {
    firstAndLast = x;
  }
};
