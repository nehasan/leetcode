// leetcode 207

import java.util.*;

class Solution {

	public Set<Integer> visiting, visited;

	Solution () {
		this.visiting = new HashSet<Integer>();
		this.visited = new HashSet<Integer>();
	}

	public boolean validateScheduling (int course, Map<Integer, List<Integer>> courseMap) {
		System.out.println("checking for course " + course);

		if (this.visited.contains(course)) {
			System.out.println("course " + course + " found in visited set so terminating and returning true");
			return true;
		}

		if (this.visiting.contains(course)) {
			System.out.println("course " + course + " found in visiting set so terminating and returning false");
			return false;
		}

		this.visiting.add(course);
		System.out.println("course " + course + " is added to visiting set " + this.visiting);

		for (int dependant : courseMap.get(course)) {
			System.out.println("going to search for dependant course " + dependant +  " of course " + course);
			if (!validateScheduling(dependant, courseMap)) {
				return false;
			}
		}

		this.visited.add(course);
		return true;
	}

	public boolean canFinish(int numCourses, int[][] prerequisites) {

		Map<Integer, List<Integer>> courseMap = new HashMap<>();

		for (int i = 0; i < numCourses; i++) {
			courseMap.put(i, new ArrayList<Integer>());
		}

		for (int[] prerequisite : prerequisites) {
			int course = prerequisite[0];
			int dependsOn = prerequisite[1];

			List<Integer> dependants = courseMap.get(course);
			dependants.add(dependsOn);
			courseMap.put(course, dependants);
		}

		for (Map.Entry<Integer, List<Integer>> entry : courseMap.entrySet()) {
			this.visiting.clear();
			this.visited.clear();

			if (!validateScheduling(entry.getKey(), courseMap)) {
				return false;
			}

			System.out.println("---check for course " + entry.getKey() + " done!");
		}

		return true;
	}
}


class Main {
	public static void main (String[] args) {
		Solution obj = new Solution();

		// int numCourses = 2;
		// int[][] prerequisites = new int[][] {{1, 0}};
		// System.out.println(obj.canFinish(numCourses, prerequisites));

		// numCourses = 2;
		// prerequisites = new int[][] {{1, 0}, {0, 1}};
		// System.out.println(obj.canFinish(numCourses, prerequisites));

		int numCourses = 5;
		int[][] prerequisites = new int[][] {{1, 4}, {2, 4}, {3, 1}, {3, 2}};
		System.out.println(obj.canFinish(numCourses, prerequisites));
	}
}