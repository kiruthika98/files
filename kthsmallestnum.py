import java.util.Arrays;
import java.util.Collections;

class GFG
{   
    // Function to return k'th smallest 
    // element in a given array
    public static int kthSmallest(Integer [] arr, 
                                         int k) 
   {
        Arrays.sort(arr);
        return arr[k-1];
    } 
    
    public static void main(String[] args) 
    {
        Integer arr[] = new Integer[]{11, 2, 4, 6, 18};
        int k = 1;
        System.out.print( "K'th smallest element is "+
                            kthSmallest(arr, k) );     
    }
}


