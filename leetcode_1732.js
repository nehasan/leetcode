/**
 * author: Nahid Hasan Khan
 * Leet code 1732 : Find the highest altitude
 */

/**
 * Approach: Initialize netGain = highestGain as 0 as we always start from 0.
 * Maintain an array of calculated latest net gain calculatedGains = [0]
 * Iterate and take each gain from the input array, calculate the netGain gain[i] + calculatedGains[i] and push the latest \
 * gain into the calculatedGains array.
 * Take the highest from the latest netGain and current highestGain
 * return highestGain at the end of the process
 * 
 * @param {number[]} list of altitudes
 * @return {number} highest altitude gain at each i 
 */

let largestAltitude = (gain) => {

    // let initialGain = 0;
    // let highestGain = Number.MIN_VALUE;
    let netGain = 0;
    let highestGain = netGain;
    let calculatedGains = [0];

    let i = 0;
    gain.forEach(g => {
        netGain = g + calculatedGains[i];
        // console.log(`NET G: ${netGain} | CALC GAIN: ${calculatedGains[i]} | HI G: ${highestGain}`);
        highestGain = Math.max(netGain, highestGain);
        i++;
        calculatedGains.push(netGain);
    });

    // console.log(calculatedGains.join(", "));
    // console.log(highestGain);

    return highestGain;
}

let res = largestAltitude([-5,1,5,0,-7]);
// let res = largestAltitude ([-4,-3,-2,-1,4,3,2]);
console.log(`${res}`);