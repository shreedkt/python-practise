import java.util.Scanner;
class ForLoop{
    public static void main(String []arg)
    {   
        Scanner sc = new Scanner(System.in);
        int x= sc.nextInt();
        
        for(int i=1; i<=10;i++)
        {
            System.out.println(x + " x " + i + " = " + x*i);
        } 
        // int i=1;
        // while(i<=10)
        // {
        //     System.out.println(2*i);
        //     i++;
        // }
        
    }
}