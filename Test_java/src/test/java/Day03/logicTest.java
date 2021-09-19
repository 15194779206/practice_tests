package Day03;

import java.util.Scanner;

public class logicTest {
    public static void main(String args[]){
        Scanner scan=new Scanner(System.in);
        System.out.print("请输入英语成绩：");
        double enScore=scan.nextDouble();
        System.out.print("请输入音乐成绩：");
        double muScore=scan.nextDouble();
//        && 与   ||或  ！非
        boolean socre =enScore>=85&&muScore>=60;
        System.out.println("可以获得漫画本吗？"+socre);
    }
}