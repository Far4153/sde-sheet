
originalArray = [1, 2, 3, 4, 5];

// Shallow array
const shallowArray = originalArray;
const deepArray = originalArray.slice();

// Change the value of an element in the shallow array
shallowArray[0] = 30;
deepArray[0]=20;

// Log the original array and the shallow array
console.log(originalArray); // [10, 2, 3, 4, 5]
console.log(shallowArray); // [10, 2, 3, 4, 5]
console.log(deepArray); // [10, 2, 3, 4, 5]