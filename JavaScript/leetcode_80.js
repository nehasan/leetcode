/**
 * Leetcode 80: Remove Duplicates from Sorted Array II
 * Author: Nahid Hasan Khan
 * Date: Aug 20 2025
 */

/**
 * Algorithm Design:
 * First iteration:
 * Initialize currNum = nums[i] and maxCount = 1
 * Iterate over the nums and when currNum != nums[i], place currNum = nums[i] and reset count to 1 and continue iteration
 * Else increase the count, count++ and if the count = 2 then place nums[i] = None/null/nil/undefined/-10001 (because , -10^4 < nums[i] < 10^4)
 * Second Iteration:
 * If nums[i] is None/null/undefined/-10001, then iterate from that point to find the next number and place it there as nums[i] = nums[j]
 * Also do not forget to make it None/null... , so nums[j] = None/null...
 * Break this iteration to find the next nums[i] = None/null... to be replaced with nums[j]
 */

/**
 * Pseudo code:
 * curr -> nums[0]
 * count -> 1
 * for n in nums
 *  if curr != n
 *    curr -> n
 *    count -> 1
 *    cont
 *  count -> count + 1
 *  if count > 2
 *    n -> null
 * 
 * for n in nums
 *  i = n.index
 *  if n = null
 *    j = i
 *    while true
 *      if nums[j] = a number
 *        n -> nums[j]
 *        nums[j] -> null
 */

const removeDuplicates = (nums) => {
  if (nums.length <= 2) return nums.length;
  
  let curr = nums[0];
  let count = 1;
  let writeIndex = 1;
  
  // Method 1: Using for...of with index (ES6+)
  for (let i = 1; i < nums.length; i++) {
    if (curr !== nums[i]) {
      curr = nums[i];
      count = 1;
      nums[writeIndex] = nums[i];
      writeIndex++;
    } else {
      count++;
      if (count <= 2) {
        nums[writeIndex] = nums[i];
        writeIndex++;
      }
    }
  }
  console.log(nums);
  return writeIndex;
};

const removeDuplicates2 = (nums) => {
  if (nums.length <= 2) return nums.length;

  let curr = nums[0];
  let count = 1;
  // let writeIndex = 1;

  for (let i = 1; i < nums.length; i++) {
    if (curr != nums[i]) {
      curr = nums[i];
      count = 1;
    } else {
      count++;
      if (count > 2) {
        nums[i] = null;
      }
    }
  }

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] == null) {
      for (let j = i + 1; j < nums.length; j++) {
        if (nums[j] != null) {
          nums[i] = nums[j];
          nums[j] = null;
          break;
        }
      }
    }
  }

  console.log(nums);
  return nums.length;
}

// console.log(removeDuplicates([1, 1, 1, 2, 2, 3]));
// console.log(removeDuplicates([0,0,0,1,1,1,1,2,3,3,3]));

console.log(removeDuplicates2([1, 1, 1, 2, 2, 3]));
console.log(removeDuplicates2([0,0,0,1,1,1,1,2,3,3,3]));

/*
// Alternative methods to iterate with index:

// Method 2: Traditional for loop (most common)
const iterateWithForLoop = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    console.log(`Index: ${i}, Value: ${arr[i]}`);
  }
};

// Method 3: Using forEach with index
const iterateWithForEach = (arr) => {
  arr.forEach((value, index) => {
    console.log(`Index: ${index}, Value: ${value}`);
  });
};

// Method 4: Using for...in (iterates over indices as strings - NOT recommended for arrays)
const iterateWithForIn = (arr) => {
  for (let index in arr) {
    console.log(`Index: ${index}, Value: ${arr[index]}`);
    // Note: index is a string, not a number
  }
};

// Method 5: Using for...of with entries() (ES6+)
const iterateWithForOf = (arr) => {
  for (let [index, value] of arr.entries()) {
    console.log(`Index: ${index}, Value: ${value}`);
  }
};

// Method 6: Using map with index
const iterateWithMap = (arr) => {
  arr.map((value, index) => {
    console.log(`Index: ${index}, Value: ${value}`);
  });
};

// Test the different methods
const testArray = [1, 2, 3, 4, 5];

console.log("Method 1: Traditional for loop");
iterateWithForLoop(testArray);

console.log("\nMethod 2: forEach with index");
iterateWithForEach(testArray);

console.log("\nMethod 3: for...of with entries");
iterateWithForOf(testArray);

console.log("\nMethod 4: for...in (not recommended for arrays)");
iterateWithForIn(testArray);

console.log("\nMethod 5: map with index");
iterateWithMap(testArray);
*/