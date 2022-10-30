import java.util.*;

public class IfElse{
    public static void main(String[] args){
        // System.out.println("hello world  " + Arrays.toString(args));
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        
        if(x<10)
        {
            System.out.println("Number is less than 10");
        } else{
            System.out.println("Number is Greater than 10");
        }
    }
}