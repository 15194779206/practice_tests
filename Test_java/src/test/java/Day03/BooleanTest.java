package Day03;

import java.util.Scanner;

public class BooleanTest {
    public static void main(String args[]){
        double mingScore=80;
        System.out.print("输入你的成绩：");
        Scanner scan=new Scanner(System.in);
        double score=scan.nextDouble();
        boolean b=mingScore>score;
        System.out.println("小明成绩比别人高是"+b);
    }
}
