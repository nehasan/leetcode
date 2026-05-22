// leetcode 322

import java.util.*;

class Solution {
	HashMap<Integer, Integer> memo;

	Solution () {
		this.memo = new HashMap<Integer, Integer>();
	}

	public int dpTopDown(int[] coins, int amount) {
		if (this.memo.containsKey(amount)) {
			return this.memo.get(amount);
		}

		int minCoins = Integer.MAX_VALUE;

		for (int coin : coins) {
			int diff = amount - coin;
			if (diff < 0) {
				break;
			}
			minCoins = Math.min(minCoins, 1 + dpTopDown(coins, diff));
			this.memo.put(amount, minCoins);
		}

		return this.memo.get(amount);
	}

	public int dpBottomUp(int[] coins, int amount) {
		int minCoins = Integer.MAX_VALUE;

		for (int i = 1; i < amount + 1; i++) {
			for (int coin : coins) {
				int diff = i - coin;

				if (diff < 0) {
					break;
				}

				minCoins = Math.min(minCoins, 1 + this.memo.get(diff));
			}

			this.memo.put(i, minCoins);
		}

		if (this.memo.get(amount) < Integer.MAX_VALUE) {
			return this.memo.get(amount);
		}

		return -1;
	}

	public int coinChange(int[] coins, int amount) {
		Arrays.sort(coins);
		this.memo.put(0, 0);
		this.memo.put(1, 1);

		// int minChange = dpTopDown(coins, amount);
		// if ( minChange < Integer.MAX_VALUE) {
		// 	return minChange;
		// }

		// return -1;

		return dpBottomUp(coins, amount);
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		int[] coins = new int[] {1,2,5};
		int amount = 11;
		System.out.println(obj.coinChange(coins, amount));
	}
}