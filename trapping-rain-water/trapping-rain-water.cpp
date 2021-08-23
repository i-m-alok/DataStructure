class Solution {
public:
    int trap(vector<int>& height) {
        int totalCount=0;
        int firstPointer=0;
        int secondPointer=1;
        if(height.size()<3) return 0;
        while(firstPointer<height.size() && secondPointer<height.size()){
            int firstValue = height[firstPointer];
            if(firstValue<=height[secondPointer]){
                firstPointer++;
                secondPointer++;
            }else if(firstValue>height[secondPointer]){
                int temp=secondPointer;
                while(height[temp]<firstValue && temp+1<height.size()){
                    temp++;
                    if(height[temp]>=height[secondPointer]){
                        cout<<"sec "<< secondPointer<<" temp "<<temp<<endl;
                        secondPointer=temp;
                    }
                }
                cout<<firstPointer<<"  "<<temp<<"==>"<<endl;
                if(temp+1>=height.size() && temp-firstPointer+1>=3 && secondPointer!=firstPointer){
                    temp=secondPointer;
                }
                int totalBlock = min(firstValue,height[temp])*(temp-firstPointer+1);
                cout<<firstPointer<<"  "<<temp<<"Pre"<<totalBlock<<endl;
                for(int i=firstPointer;i<=temp;i++){
                    totalBlock-= min(min(firstValue,height[temp]),height[i]);
                }
                cout<<firstPointer<<"  "<<temp<<"  "<<totalBlock<<endl;
                totalCount+=totalBlock;
                if(totalBlock==0) temp=firstPointer+1;
                firstPointer=temp;
                secondPointer=temp+1;
            }
        }
        return totalCount;
    }
};