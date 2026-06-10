class RecentCounter {
  requests: number[];
  pointerOne: number;
  count: number;

  constructor() {
    this.count = 0;
    this.pointerOne = 0;
    this.requests = new Array();
  }

  ping(t: number): number {
    this.requests.push(t);
    this.count++;
    if (this.count == 1) return 1;
    while (true) {
      let first = this.requests[0];
      let last = this.requests[this.count - 1];

      if (last - first > 3000) {
        this.requests.shift();
        this.count--;
      } else {
        return this.count;
      }
    }
  }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */

var obj = new RecentCounter();
console.log(obj.ping(1));
console.log(obj.ping(100));
console.log(obj.ping(200));
console.log(obj.ping(3000));
console.log(obj.ping(3010));
console.log(obj.ping(3020));
