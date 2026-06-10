/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function (nums) {
  // let sum = 0;
  let leftSideTotal = 0;
  let rightSideTotal = 0;
  nums.forEach((n) => {
    rightSideTotal += n;
  });

  let i = 0;
  for (n of nums) {
    rightSideTotal -= n;
    if (leftSideTotal === rightSideTotal) return i;
    leftSideTotal += n;
    i++;
  }

  return -1;
};


// nums = [1, 7, 3, 6, 5, 6] // expected output : 3
// nums = [1, 2, 3]; // expected output : -1
// nums = [1, 1]; // expected output : -1
// nums = [1, 1, 1]; // expected output : 1
// nums = [1, 0, 1]; // expected output : 1
nums = [0, 1]; // expected output : 1
console.log(pivotIndex(nums));