class Solution {
public:
    int kthGrammar(int n, int k) {
        return findKthElement(n-1, k, 0);
    }
    
    int findKthElement(int n, int k, int current){
        if(n==0){
            return 0;
        }
        int mid = pow(2, n)/2;
        if(k<=mid){
            return findKthElement(n-1, k, current);
        }else{
            return (int)(!findKthElement(n-1, k-mid, current));
        }
    }
};