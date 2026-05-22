/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {
    arr = Array();

    for(var i = 0; i < s.length; i++) {
        if (s.charAt(i) === '*') {
            arr.pop();
        } else {
            arr.push(s.charAt(i));
        }
    }

    return arr.join('');
};

s = 'leet**cod*e' // output 'lecoe'
console.log(removeStars(s));