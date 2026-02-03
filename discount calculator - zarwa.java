import java.util.*;
public class Main
{
    private static Scanner input; 
    public static void main(String[] args)
    {
        input = new Scanner (System.in) ; 
        double purchaseValue, discount; 
        discount=0; 
        System.out .println("enter value of goods purchased: "); 
        purchaseValue = input.nextDouble () ; 
        if (purchaseValue>=100) 
            discount = purchaseValue * 0.2; 
            System.out.println("Your discount is: " + discount);
            double bill = purchaseValue-discount;
            System.out.println("Your Bill is: " + bill);
            second();
            System.out.println("Back to main");
            System.out.println("Bye");
    }
    
    public static void second()
    {
    System.out .println("I am in the second procedure now ");
   
    }
}