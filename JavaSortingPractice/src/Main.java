public class Main {
    public static void main(String[] args) {
        int[] arr = {17, 16, 33, 1};
        SelectionSort ss = new SelectionSort(arr);
        System.out.println("Unsorted array: ");
        int count = 0;
        for(int i: arr){
            if (count == arr.length-1){
                System.out.println(i + " ");
            }else{
                System.out.print(i + ", ");
                count++;
            }
        }
        count = 0;
        ss.perform();
        System.out.println("Sorted array: ");
        for (int i: arr){
            if (count == arr.length-1){
                System.out.println(i + " ");
            }else{
                System.out.print(i + ", ");
                count++;
            }
        }
    }
}
