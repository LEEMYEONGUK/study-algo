package 조건문;

import java.util.Scanner;

public class B2480 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        if (a != b && b != c && c != a) {
            if (a > b && a > c) {
                System.out.println(a * 100);
            } else if (b > a && b > c) {
                System.out.println(b * 100);
            } else if (c > a && c > b) {
                System.out.println(c * 100);
            }
        } else if (a == b && b != c) {
            System.out.println(1000 + 100 * a);
        } else if (b == c && b != a) {
            System.out.println(1000 + 100 * b);
        } else if (a == c && a != b) {
            System.out.println(1000 + 100 * a);
        } else if (a == b && b == c) {
            System.out.println(10000 + 1000 * a);
        }


//        if (a == b && b == c) {
//            System.out.println(10000 + 1000 * a);
//        } else if (a == b || a == c) {
//            System.out.println(1000 + 100 * a);
//        } else if (b == c) {
//            System.out.println(1000 + 100 * b);
//        } else {
//            int max = Math.max(a, Math.max(b, c));
//            System.out.println(max * 100);
//        }

    }
}
