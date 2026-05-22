// Leet Code 1768 Merge Strings Alternately
// Oct 09 2023 Nahid Hasan Khan

/**
 * Algorithm uses simple array merging
 * Final word = word1[index] valid value or '' + word2[index] valid value or ''
 */

/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    // calculate the max length of the two words
    let len = Math.max(word1.length, word2.length);

    return mergeTwoWords(word1, word2, len);
};

const mergeTwoWords = (word1, word2, len) => {
    let str = '';
    for (var i = 0; i < len; i++) {
        str += (word1[i] === undefined ? '' : word1[i]) + (word2[i] === undefined ? '' : word2[i]);
    }

    return str;
}

word1 = 'abc'
word2 = 'pqrs'

console.log(mergeAlternately(word1, word2))