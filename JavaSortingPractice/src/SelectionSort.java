public class SelectionSort {

    int[] arr;

    public SelectionSort(int[] arr){
        this.arr = arr;
    }

    public void perform(){
        for(int i=0; i<arr.length-1; i++){
            for(int j=i+1; j<arr.length; j++){
                if(arr[j]<arr[i]){
                    swap(arr, i, j);
                }
            }
        }
    }

    public void swap(int[] swapArr, int a, int b){
        int temp = swapArr[a];
        swapArr[a] = swapArr[b];
        swapArr[b] = temp;
    }
}
