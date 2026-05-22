// leetcode 433

import java.util.*;

class Solution {
	public List<String> findOneDistanceGenes(String gene, Set<String> geneSet) {
		StringBuffer tempGene;
		List<String> oneDistanceGenes = new ArrayList<>();

		for (int i = 0; i < gene.length(); i++) {
			tempGene = new StringBuffer(gene);
			char[] choices = {'A', 'C', 'G', 'T'};
			for (int j = 0; j < choices.length; j++) {
				tempGene.setCharAt(i, choices[j]);
				if (geneSet.contains(tempGene.toString())) {
					oneDistanceGenes.add(tempGene.toString());
					geneSet.remove(tempGene.toString());
				}
			}
		}

		return oneDistanceGenes;
	}

	/*
	* Similar approach as leetcode 127 word ladder
	* Time complexity: O(4*n*m) where n is the number of characters of a string (currGene) and m is the number of oneDistanceGenes to be visited
	*/

	public int minMutation(String startGene, String endGene, String[] bank) {
		Set<String> geneSet = new HashSet<>();
		Queue<String> geneQueue = new LinkedList<>();

		for (String gene: bank) {
			geneSet.add(gene);
		}

		if (!geneSet.contains(endGene)) {
			return -1;
		}

		geneSet.add(startGene);
		geneQueue.add(startGene);
		int level = 0;

		while(!geneQueue.isEmpty()) {
			int qSize = geneQueue.size();

			while(qSize-- > 0) {
				String currGene = geneQueue.poll();
				geneSet.remove(currGene);

				List<String> oneDistanceGenes = findOneDistanceGenes(currGene, geneSet);

				for (String oneDistanceGene : oneDistanceGenes) {
					if (!geneSet.contains(oneDistanceGene)) {
						if (oneDistanceGene.equals(endGene)) {
							return level + 1;
						} else {
							geneQueue.add(oneDistanceGene);
						}
					}
				}
			}

			level++;
		}

		return -1;
	}
}


class Main {
	public static void main(String[] args) {
		Solution obj = new Solution();

		// String startGene = "AACCGGTT", endGene = "AACCGGTA";
		// String[] bank = {"AACCGGTA"};

		String startGene = "AACCGGTT", endGene = "AAACGGTA";
		String[] bank = {"AACCGGTA","AACCGCTA","AAACGGTA"};

		System.out.println(obj.minMutation(startGene, endGene, bank));
	}
}