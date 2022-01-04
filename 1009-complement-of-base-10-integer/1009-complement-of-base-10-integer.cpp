class Solution {
public:
    int bitwiseComplement(int n) {
        if(n==0){
            return 1;
        }
        int result = 0;
        int count = 0;
        bool remainder = 0;
        while(n>0){
            remainder = n%2;
            // cout<<(int)(!(remainder))*pow(2, count)<< "   "<< n<<"\n";
            result += (int)(!(remainder))*pow(2, count);
            
            n = n/2;
            count++;
        }
        return result;
    }
};