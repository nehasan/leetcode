// leet code 394. decode string
// nahid hasan khan
// Oct 08 2023

/**
 * Algorithm follows stack push pop rules
 * Iterate through each element of the string
 * If it is a number then make the number until we get a '['
 * If it is a '[' that means number building is done and can be pushed to a stackNums
 * If other than ']' char, we place them in a stackArr
 * If we get ']' then we need to iterate back to find the closest '[', and whatever in between
 * They must be bind together, reverese them and push back to the same stackArr with stackNums.last() times repeated
 */

/**
 * Returns the decoded string according to the rules
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    let stackArr = [];
    let stackNums = [];
    let number = '';

    for (const c of s) {
        if (c === ']') {
            let tempArr = [];
            let stackedValue = stackArr.pop();

            // pop stacked arr until we get '['
            while (stackedValue !== '[') {
                tempArr.push(stackedValue);
                stackedValue = stackArr.pop();
            }

            // reverse the temp arr
            let tempStr;
            tempStr = tempArr.reverse().join('');

            // append the tempStr at the end of the same stack
            let loop = stackNums.pop();
            for (var i = 0; i < loop; i++) {
                stackArr.push(tempStr);
            }

        } else if (c >= '0' && c <= '9' ) {
            number += `${c}`;
        } else if (c === '[') {
            stackArr.push(c);
            stackNums.push(parseInt(number));
            number = '';
        } else {
            stackArr.push(c);
        }
    }

    return stackArr.join('');
};

console.log(decodeString('3[a2[bc]]ca'));
// console.log(decodeString('3[a]2[bc]'));