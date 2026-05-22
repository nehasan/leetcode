# leetcode 721

from typing import List
from collections import defaultdict
from collections import deque

class Solution:
	'''
	Approch, using hashmaps and graph traversal
	- Read all the emails and create a hashmap that maps email -> [account_index]
	- For example the test case below produce a hash map {'e1':[0], 'e2':[1], 'e3': [0, 1] ... }
	- Now read the values of the above hashmap and make a graph out of it.
	- For example for the above values email e3 contains in both 0 and 1 index or that means both are connected
	- While making the graph make sure adjecent values are unique
	- Now read the indexGraph and apply BFS or DFS to find all the connected indices, merge their sorted emails
	- along with the name and create a new list and then return
	'''
	def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
		
		emailToIndices = defaultdict(list)

		for index, account in enumerate(accounts):
			for email in account[1:]:
				emailToIndices[email] += [index]

		indexGraph = defaultdict(list)

		for key, indices in emailToIndices.items():
			if (len(indices)) > 1:
				for i, index in enumerate(indices):
					otherIndicesExceptIndex = [x for j, x in enumerate(indices) if j != i]
					for n in otherIndicesExceptIndex:
						if n not in indexGraph[index]:
							indexGraph[index] += [n]
			else:
				indexGraph[indices[0]] += []

		visitedGlobal = set()
		res = []

		for k, v in indexGraph.items():
			indexQ = deque()
			indexQ.append(k)
			currAccName = []
			currAccEmails = set()

			while(len(indexQ) > 0):
				curr = indexQ.popleft()

				if curr not in visitedGlobal:
					currAccName = [accounts[curr][0]];
					s = set(accounts[curr][1:])
					currAccEmails = currAccEmails.union(s)

					for adjecent in indexGraph[curr]:
						indexQ.append(adjecent)

					visitedGlobal.add(curr)

			if len(currAccName) > 0:
				res.append(currAccName + sorted(list(currAccEmails)))

		return res




obj = Solution()
# accounts = [
# 	["J1", "e1", "e2", "e3"],
# 	["J1", "e3", "e4", "e5"],
# 	["B1", "ee1", "ee2", "ee3"],
# 	["M1", "eee1", "eee2", "eee3"],
# 	["B1", "ee2", "ee3"]
# ]
# obj.accountsMerge(accounts)

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
obj.accountsMerge(accounts)

# accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# obj.accountsMerge(accounts)