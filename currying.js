function funcName(a) {
    return function (b) {
       return a * b;
    }
 }
 console.log(funcName(2)(3));