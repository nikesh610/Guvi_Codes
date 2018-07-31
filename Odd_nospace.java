
import java.util.*;
import java.lang.*;
import java.io.*;


class Odd_nospace
{ 
	public static void main (String[] args) throws java.lang.Exception 
	{
		
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
        int b=sc.nextInt();
        int[] arr=new int[b-a+1];
        int j=0;
		for(int i=a+1;i<b;i++)
		   { 
                  if(i%2!=0)
                {
                    arr[j]=i; //Storing the Odd Numbers in the Array
                    j++;
                }
           }
           for(int i=0;i<j;i++)
            {
                if(i!=j-1)
                    {
                        System.out.print(arr[i]+" ");
                    }
                    else{
                        System.out.print(arr[i]);
                    }
            }
	}
}
