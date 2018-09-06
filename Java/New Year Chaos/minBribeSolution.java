/*
Project: New Year Chaos
This: minBribeSolution.java
Author: C Robinson
Date: 06 Sep 2018
Purpose: Solve New Year Chaos problem. What this problem uses:
                - Bubble Sort
                - Counter for moves per number
                - Counter for minimum moves
                - For/if to print out results
                
 This solution does not pass all 12 tests.
 */
public class minBribeSolution {
    // Complete the minimumBribes function below.
    static void minimumBribes(int[] q) {
        int n = q.length;
        int c[] = new int[n];
        int b = 0, d = 0;
        for (int i = 0; i < n-1; i++){
            for (int j = 0; j < n-i-1; j++){
                if (q[j] > q[j+1]){
                    c[q[j]-1]++;
                    int temp = q[j];
                    q[j] = q[j+1];
                    q[j+1] = temp;
                    b++;
                }
            }
        }
        for(int i = 0; i < c.length; i++){
            if(c[i] > 2){
                System.out.println("Too chaotic");
                d++;
                break;
            }
        }
        if(d < 1){
            System.out.println(b);
        }       
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] q = new int[n];

            String[] qItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int qItem = Integer.parseInt(qItems[i]);
                q[i] = qItem;
            }
            minimumBribes(q);
        }

        scanner.close();
    }
}
