public class Lins {
  void found(int arr[],int size,int target){
        for(int i=0; i<size; i++){
            System.out.print(arr[i]+" ");
            if(arr[i] ==target) {
                System.out.println(i);
        
            }
        }
        return -1;
    }
          public static void main(String[] args) {
        int arr[]={1,5,10,15,20};
        int size=5;
        int target =15;

        Lins pbj=new Lins();
        pbj.found(arr,size,target);

    }
    
}

