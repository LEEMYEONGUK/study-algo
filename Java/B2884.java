import java.util.Scanner;

public class B2884 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hour = sc.nextInt();
        int minute = sc.nextInt();

        if (hour == 0 && minute < 45){
            hour = 23;
            minute = minute + 60 - 45;
        } else if (minute >= 45) {
            minute -= 45;
        } else if (minute < 45) {
            hour -= 1;
            minute = minute + 60 - 45;
        }

        System.out.print(hour);
        System.out.print(" ");
        System.out.print(minute);
    }
}
