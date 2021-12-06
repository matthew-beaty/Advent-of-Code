// Advent of Code - 2021
// Day 6

let input = [
  3, 5, 3, 5, 1, 3, 1, 1, 5, 5, 1, 1, 1, 2, 2, 2, 3, 1, 1, 5, 1, 1, 5, 5, 3, 2,
  2, 5, 4, 4, 1, 5, 1, 4, 4, 5, 2, 4, 1, 1, 5, 3, 1, 1, 4, 1, 1, 1, 1, 4, 1, 1,
  1, 1, 2, 1, 1, 4, 1, 1, 1, 2, 3, 5, 5, 1, 1, 3, 1, 4, 1, 3, 4, 5, 1, 4, 5, 1,
  1, 4, 1, 3, 1, 5, 1, 2, 1, 1, 2, 1, 4, 1, 1, 1, 4, 4, 3, 1, 1, 1, 1, 1, 4, 1,
  4, 5, 2, 1, 4, 5, 4, 1, 1, 1, 2, 2, 1, 4, 4, 1, 1, 4, 1, 1, 1, 2, 3, 4, 2, 4,
  1, 1, 5, 4, 2, 1, 5, 1, 1, 5, 1, 2, 1, 1, 1, 5, 5, 2, 1, 4, 3, 1, 2, 2, 4, 1,
  2, 1, 1, 5, 1, 3, 2, 4, 3, 1, 4, 3, 1, 2, 1, 1, 1, 1, 1, 4, 3, 3, 1, 3, 1, 1,
  5, 1, 1, 1, 1, 3, 3, 1, 3, 5, 1, 5, 5, 2, 1, 2, 1, 4, 2, 3, 4, 1, 4, 2, 4, 2,
  5, 3, 4, 3, 5, 1, 2, 1, 1, 4, 1, 3, 5, 1, 4, 1, 2, 4, 3, 1, 5, 1, 1, 2, 2, 4,
  2, 3, 1, 1, 1, 5, 2, 1, 4, 1, 1, 1, 4, 1, 3, 3, 2, 4, 1, 4, 2, 5, 1, 5, 2, 1,
  4, 1, 3, 1, 2, 5, 5, 4, 1, 2, 3, 3, 2, 2, 1, 3, 3, 1, 4, 4, 1, 1, 4, 1, 1, 5,
  1, 2, 4, 2, 1, 4, 1, 1, 4, 3, 5, 1, 2, 1,
];

// testing for a count map
let fishCounts = {
  zero: 0,
  one: 1,
  two: 0,
  three: 2,
  four: 0,
  five: 2,
  six: 0,
  seven: 0,
  eight: 0,
  total: 5,
};

let testInput = [5];

function simulateDays(numDays) {
  for (let day = 0; day < numDays; day++) {
    let newFish = [];

    input.forEach((currFish, index) => {
      // reset fish to max spawn days (6), and populate new fish
      // note - new fish do not count down a day until next day

      if (currFish == 0) {
        input[index] = 6;
        newFish.push(8);
      } else {
        input[index]--;
      }

      // mix new fish with existing fish at end of each day, clear newFish
    });
    input = input.concat(newFish);
    newFish = [];
  }
  return input;
}

// part 1 answer:
// console.log(simulateDays(200).length);

// part 2
function projectFish(numDays) {
  let startFishMap = {
    zero: 0,
    one: 0,
    two: 0,
    three: 0,
    four: 0,
    five: 0,
    six: 0,
    seven: 0,
    eight: 0,
    total: 0,
  };
  // convert input to fishMap
  for (let fish of input) {
    switch (true) {
      case fish == 1:
        startFishMap.one++;
        break;
      case fish == 2:
        startFishMap.two++;
        break;
      case fish == 3:
        startFishMap.three++;
        break;
      case fish == 4:
        startFishMap.four++;
        break;
      case fish == 5:
        startFishMap.five++;
        break;
    }
    startFishMap.total++;
  }

  let tempFishCounts = { ...startFishMap };

  for (let day = 0; day < numDays; day++) {
    let spawn = 0;

    if (tempFishCounts.zero > 0) {
      spawn = tempFishCounts.zero;
    }

    tempFishCounts = {
      zero: tempFishCounts.one,
      one: tempFishCounts.two,
      two: tempFishCounts.three,
      three: tempFishCounts.four,
      four: tempFishCounts.five,
      five: tempFishCounts.six,
      six: tempFishCounts.seven + tempFishCounts.zero,
      seven: tempFishCounts.eight,
      eight: spawn,
      total: tempFishCounts.total + spawn,
    };
  }

  return tempFishCounts.total;
}

console.log(projectFish(256));
