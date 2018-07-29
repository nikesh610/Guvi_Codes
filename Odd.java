/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Odd
{
	public static void main (String[] args) throws java.lang.Exception
	{
	   Scanner s=new Scanner(System.in);
	   int a=s.nextInt();
	   int b=s.nextInt();
	   int[] st=new int[b-a];
	   int cnt=0;
	   for(int i=a+1;i<b;i++)
	   {
	   	if(i%2!=0)
	   	{
	   		st[cnt]=i;
	   		cnt++;
	   	}
	   }
	   for (int i=0;i<cnt;i++)
	   {
	   	if(i==cnt-1)
	   	  System.out.print(st[i]);
	   
	   else
	   {
	   	System.out.print(st[i]+" ");
	   }
	}
}
}
