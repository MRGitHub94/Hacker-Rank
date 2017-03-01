// Javascript coding questions

function temporarySwapHalf(array) {
    var left = null;
    var right = null;
    var length = array.length;
    for (left = 0; left < length/2; left++) {
        right = length - 1 - left;
        var temp = array[left];
        array[left] = array[right];
        array[right] = temp;
    }
    return array;
}

console.log(temporarySwapHalf([1,2,3]));

var reverse = function(arr) {
    var result = [];
    ii = arr.length;
    for (var i = ii - 1; i !== 0; i--) {
        result.push(arr[i]);
    }
    return result;
}

console.log(reverse([1,2,3]));

// Getting even numbers out of an array

function evenList(a) {
    var b = [];
    for (var i =0; i < a.length; i++) {
    if (a[i]%2 === 0){
        b.push(a[i]);
        }
    }
    return b;
}

console.log(evenList([0,1,2,3,4,5,6,7,8,9]));

// Bubble sort
function bubbleSort(a) {
    var swapped;
    do {
        swapped = false;
        for (var i = 0; i < a.length-1; i++) {
            if (a[i] > a[i+1]) {
                var temp = a[i];
                a[i] = a[i+1];
                a[i+1] = temp;
                swapped = true;
            }
        }
    } while (swapped);
    return a;
} 
console.log(bubbleSort([34,203,3,57,89]));

// You are given a square matrix of size NxN. Calculate the absolute difference 
// of the sums across the two main diagonals. 

// 3 
// 11 2 4
// 4 5 6
// 10 8 -12

// 15
// 11 + 5 + -12 = 4
// 4 + 5 + 10 = 19
// abs(4 - 19) = 15
var n = parseInt(
[11, 2, 4],
[4, 5, 6]
[10, 8, -12]);
var suma = 0, sumb = 0;
for(var i = 0; i < n; i++){
   var line = n;
   suma += Number(line[i]);
   sumb += Number(line[n-i-1]);
}
console.log(Math.abs(sumb-suma));
// console.log(processData(
// [11, 2, 4],
// [4, 5, 6]
// [10, 8, -12]));

// function processData(a){
// var backSlash = 0;
// var forwardSlash = 0;
// for (var i = 0; i < n; i++) {
//     for (var j = 0; j < n; j++) {
//         if (i == j) {
//             backSlash += a[i][j];
//         }
//         if (i + j == n-1) {
//             forwardSlash += a[i][j];
//             }
//         }
//     }
// console.log(Math.abs(backSlash - forwardSlash));
// }

// console.log(processData(
// [11, 2, 4],
// [4, 5, 6]
// [10, 8, -12]));

// Add to zero - Given a list of ints, return True if any two numbers in list sum to 0
// Datastructur Design 

// add the number to an internal data structure
// find if there exists a pair of numbers which sum is equal to the value

var elements = [];
function add(number) {
    if (elements[number] != null) {
        elements[number] = elements[number] + 1;
    } else {
        elements[number] = 1;
    }
}

function find(value) {
    for (var i in elements) {
        var target = value - i;
        if (elements[target] != null) {
            if (i == target && elements[target] < 2) {
                continue;
            }
            return true;
        }
    }
    return false;
}

add(1);
add(-1);
add(3);
console.log(find(0));
// returns indices of the two numbers 
function twoSum(ints, target) {
    var map = [];
    var result = [];

    for (var i = 0; i < ints.length; i++) {
        if (map[ints[i]] != null) {
            console.log("map", map);
            console.log("map[ints[i]])", map[ints[i]]);
            console.log("i", i);
            index = map[ints[i]];
            result[0] = index + 1;
            console.log("result[0]",result[0]);
            result[1] = i + 1;
            break;
        } else {
            map[target - ints[i]] = i;
        }
    }
    return result;
}
console.log(twoSum([1,2,3,4,5,6,7],5));
console.log(twoSum([1,2,3,-1, -2, -3],0));
// Concatenate one list at the end of the other

// Return n unique random numbers from a list

// print a series of message of "fizz", "buzz", and "fizzbuzz"

// Is a number a prime number?

// Is a word a palindrome?

// Implementation of max()

// Given three integers, return the largest one

// translate a text to pig latin

// 