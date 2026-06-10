import java.util.*;

class UglyNumber {
    List<Integer> uglies;
    public void generateUglies() {
        HashMap<Integer, Integer> ugliesMap = new HashMap<>();
        uglies = new ArrayList<>();

        int[] factors = new int[]{ 2, 3, 5 };
        int n = 2;
        int i = 0;

        while (i < 1691) {
            int m = n;
            for (int f : factors) {
                while (m > 1) {
                    if (m % f == 0) {
                        m = (int) m / f;

                        if (ugliesMap.containsKey(m)) {
                            m = 0;
                            break;
                        }
                    } else {
                        break;
                    }
                    
                }
            }

            if (m <= 1) {
                ugliesMap.put(n, n);
                uglies.add(n);
                i++;
            }
            n++;
        }


    }
    public int nthUglyNumber(int n) {
        generateUglies();
        System.out.println(uglies.get(n));
    }

    public void run(){}

    public static void main(String[] args) {
    
    }
}