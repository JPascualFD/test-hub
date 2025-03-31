package algoritmos;

import java.util.Arrays;

public class ArraySort{
    public static void main(String[] args) {
        sortMyArray(new int[]{10,1,4,5,2,1});
    }

    public static int[] sortMyArray(int[] arr){
        Arrays.sort(arr);
        return arr;
    }
}