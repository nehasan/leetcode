// import java.util.Set;
// import java.util.HashSet;
import java.util.*;

public class Main {
	public static void main(String[] args) {
		Set<String> set = new HashSet<>();
		// set.add(new int[] {0,1});
		// set.add(new int[] {0,2});
		int i = 0, j = 2;
		set.add(i + "" + (j - 1));
		set.add(i + "" + j);
		
		// int[] coor = new int[] {0,1};
		System.out.println(set);
		if (set.contains(i + "" + j)) {
			System.out.println("Exists");
		} else {
			System.out.println("Does not exists");
		}

		int[][] points = new int[][] {{1, 3}, {-2, 2}};
		for (int[] point: points) {
			int x = point[0];
			int y = point[1];
			System.out.println(Math.pow((0 - 3), 2));
			double xDistance = (double)Math.sqrt(Math.pow((0 - x), 2.0)), yDistance = (double)Math.sqrt(Math.pow((0 - y), 2.0));

			System.out.println("xDistance : " + xDistance + " yDistance" + yDistance);

			double distance = xDistance + yDistance;

			System.out.println("distance : " + distance);
		}
	}
}