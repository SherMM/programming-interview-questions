import java.util.concurrent.ThreadLocalRandom;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class DutchFlag {

    public static int[] groupByPivot(int[] numbers, int pivot) {
        int index = 0, i;
        int[] ordered = new int[numbers.length];
        for (i = 0; i < numbers.length; i++) {
            if (numbers[i] < pivot) {
                ordered[index] = numbers[i];
                index++;
            }
        }

        for (i = 0; i < numbers.length; i++) {
            if (numbers[i] == pivot) {
                ordered[index] = numbers[i];
                index++;
            }
        }

        for (i = 0; i < numbers.length; i++) {
            if (numbers[i] > pivot) {
                ordered[index] = numbers[i];
                index++;
            }
        }
        return ordered;
    }

    public static void groupByPivotInplace(int [] numbers, int pidx) {
        int pivot = numbers[pidx];
        int low = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] < pivot) {
                swap(numbers, i, low);
                low++;
            }
        }

        int high = numbers.length-1;
        for (int i = high; i >= low; i--) {
            if (numbers[i] > pivot) {
                swap(numbers, i, high);
                high--;
            }
        }
    }

    public static void swap(int [] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    public static int[] getPivotSlicePosition(int[] numbers, int pivot) {
        int[] pos = new int[2];
        int found = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == pivot) {
                if (found == 0) {
                    pos[0] = i;
                    pos[1] = i;
                    found = 1;
                } else {
                    pos[1]++;
                }
            }
        }
        return pos;
    }

    public static boolean pivotSliceIsContiguous(int[] numbers, int pivot) {
        int[] slice = getPivotSlicePosition(numbers, pivot);
        for (int i = slice[0]; i <= slice[1]; i++) {
            if (numbers[i] != pivot) {
                return false;
            }
        }
        return true;
    }

    public static boolean numbersGroupedAroundPivot(int[] numbers, int pivot) {
        int[] slice = getPivotSlicePosition(numbers, pivot);
        for (int i = 0; i < slice[0]; i++) {
            if (numbers[i] >= pivot) {
                return false;
            }
        }

        for (int i = slice[1]+1; i < numbers.length; i++) {
            if (numbers[i] <= pivot) {
                return false;
            }
        }
        return true;
    }


    public static void main(String [] args) {
        int n = Integer.parseInt(args[0]);
        int[] numbers = new int[n];
        int min = 0, max = 25;
        for (int i = 0; i < n; i++) {
            numbers[i] = ThreadLocalRandom.current().nextInt(min, max+1);
        }

        // get pivot index and pivot
        int pidx = ThreadLocalRandom.current().nextInt(0, n);
        int pivot = numbers[pidx];

        System.out.println("original array:");
        System.out.println(Arrays.toString(numbers));
        System.out.println("pivot index: " + pidx);
        System.out.println("pivot: " + pivot);
        System.out.println();
        System.out.println("new array:");
        int[] ordered = groupByPivot(numbers, pivot);
        System.out.println(Arrays.toString(ordered));
        System.out.println();
        if (pivotSliceIsContiguous(ordered, pivot) && numbersGroupedAroundPivot(ordered, pivot)) {
            System.out.println("Tests Passed");
        } else {
            System.out.println("Tests Failed");
        }

        System.out.println();
        System.out.println("original array:");
        groupByPivotInplace(numbers, pidx);
        System.out.println("new array");
        System.out.println(Arrays.toString(numbers));
        System.out.println();
        if (pivotSliceIsContiguous(numbers, pivot) && numbersGroupedAroundPivot(numbers, pivot)) {
            System.out.println("Tests Passed");
        } else {
            System.out.println("Tests Failed");
        }

    }
}