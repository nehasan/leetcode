// Leet code 605 Can Place flowers
// Nahid Hasan Khan
// Sep 12 2023 

/**
 * Returns true or false based on planting required n flowers in a flowerbed without violeting adjecent rules
 * Algorithm uses a little bit number theory and keep tracking of the consecutive values (0s)
 * In between two 1s maximum number of 1s can be placed (without violeting adjecent rules) in following rules:
 * -> Consecutive 3 0s maximum one 1s can be placed, for 5 maximum 2, for 7 maximum 3, that satisfies ((n+1)/2)-1 formula
 * -> For beginning or ending 0s it satisfies (n/2) formula, for example, [0,0,1] or [0,0,0,1]
 * -> For either above case max 1 1s can be placed
 * -> For [0] or [0,0,0] it satisfies (n/2) + 1
 * Algorithm:
 * - iterate over the flowerbed and keep track of the consecutive zeroes if it's a 0
 * - if 1 then sum up the number of used flowers with either consZeroes / 2 or ((consZeroes+1)/2)-1 formula
 * - after the whole iteration do the final check for the remining consecutive zeroes
 * - return true if number of used flowers is greater than n, else false
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    // if (flowerbed.length == 1 && n == 1) return true;

    let consecutiveZeroes = 0;
    let numberProcessed = 0;
    let flowerUsed = 0;

    for (const value of flowerbed) {

        // if 1 then apply the number theory to calculate maximum number of 1s can be placed
        // reset consZeroes count
        if (value == 1) {
            flowerUsed += (numberProcessed == 0 ? Math.floor(consecutiveZeroes / 2) : Math.floor((consecutiveZeroes + 1) / 2) - 1);
            consecutiveZeroes = 0;
            numberProcessed += 1;
        }
        // keep track of the the consZeroes count
        else {
            consecutiveZeroes += 1;
        }
    }

    // final calculation for remining consZeroes
    flowerUsed += numberProcessed == 0 ? Math.floor((consecutiveZeroes + 1) / 2) : Math.floor(consecutiveZeroes / 2);

    return flowerUsed >= n;
};

// const n = 2;
// const flowerBed = [1,0,0,0,1]; // for n = 1 out: true, for n = 2 out: false
// const flowerBed = [0,0,1,0]; // for n = 1 out: true, for n = 2 out: false
// const flowerBed = [0,0,1,0,0]; // for n = 2 out: true, for n = 3 out: false
// const flowerBed = [0,0,1,0,0,1]; // for n = 1 out: true, for n >= 2 out: false
// const n = 3, flowerBed = [0,0,0] // out: false
// const n = 1, flowerBed = [0,1,0] // out: false
// const n = 1, flowerBed = [0,0] // out: true
// const n = 1, flowerBed = [0] // out: true
// const n = 2, flowerBed = [0,0,0] // out: true
// console.log(canPlaceFlowers(flowerBed, n));