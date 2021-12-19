class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        unordered_map<int,int> countMap;
        for(int i=0;i<nums.size();i++){
            int key = nums[i];
            if(countMap[key]!=0){
                countMap[key]+=1;
            }else{
               countMap[key]=1; 
            }
        }
        vector<int> result;
        for (auto x : countMap){
          if(x.second>1){
              result.push_back(x.first);
          }  
        }
      return result;
    }
};