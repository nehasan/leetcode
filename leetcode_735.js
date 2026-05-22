/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function(asteroids) {
    let asteroidStack = Array();

    function sameDirection(asteroid1, asteroid2) {
        return ((asteroid1 > 0 && asteroid2 > 0) || (asteroid1 < 0 && asteroid2 < 0)) ? true : false
    }

    function oppositeDirection(asteroid1, asteroid2) {
        return ((asteroid1 > 0 && asteroid2 < 0) || (asteroid1 < 0 && asteroid2 > 0)) ? true : false
    }

    function collide (asteroid1, asteroid2) {
        return (asteroid1 > 0 && asteroid2 < 0) ? true : false
    }

    for (const value of asteroids) {
        // console.log(value);

        let done = false;
        while (!done) {
            const last = asteroidStack[asteroidStack.length - 1];

            // if stack is empty then push the current asteroid and done
            if (last == undefined) {
                asteroidStack.push(value);
                done = true;
            } 
            // if same direction then push the current asteroid into the stack and hit done
            else if (sameDirection(last, value)) {
                asteroidStack.push(value);
                done = true;
            } 
            // if opposite direction then
            //  - first check if last asteroid in stack is smaller then pop the asteroid and keep going for the next last
            //  - if both are equal then just pop the last one and hit done
            //  - else we keep the bigger last one as it is and hit done
            else if (oppositeDirection(last, value) && collide(last, value)) {
                if (Math.abs(last) < Math.abs(value)) {
                    asteroidStack.pop();
                } else if (Math.abs(last) == Math.abs(value)) {
                    asteroidStack.pop();
                    done = true;
                } else {
                    done = true;
                }
            } else {
                asteroidStack.push(value);
                done = true;
            }
        }
    }

    return asteroidStack;
};

// asteroids = [5, 10, -5]; // output: [5, 10]
// asteroids = [5, -5];     // output: []
// asteroids = [-5, 5];        // output: [-5, 5]
// asteroids = [10,2,-5];   // output: [10]
// asteroids = [10];        // output: [10]
// asteroids = [-10, 10, 10];        // output: [10]
// asteroids = [10, 9, -10];        // output: []
// asteroids = [-2, -1, 1, 2];            // output: [-2, -1, 1, 2]
console.log(asteroidCollision(asteroids));