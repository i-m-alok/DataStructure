class Solution {
public:
    string decodeString(string s) {
        stack<int> nums;
        // stack<char> sign;
        stack<string> str;
        string temp = "";
        int count = 0;
        for(int i= 0;i<s.size(); i++){
            if('['==s[i]){
                // sign.push(s[i]);
                str.push(temp);
                temp = "";
            }else if(s[i]>=48 && s[i]<=57){
                // if(temp!=""){
                //     str.push(temp);
                //     temp="";
                // }
                nums.push(s[i]-48);
                cout<< count << " count ";
                if(s[i+1]>=48 && s[i+1]<=57){
                    count++;
                }else{
                    int power = count;
                    int c_num = 0;
                    while(count>=0){
                        c_num+=nums.top()*pow(10, power-count);
                        nums.pop();
                        count--;
                    }
                    nums.push(c_num);
                    count=0;
                }
                
            }else if(']'==s[i]){
                
                int c = nums.top();
                nums.pop();
                // sign.pop();
                string sub = str.top();
                str.pop();
                for(int j=1;j<=c;j++){
                    cout << temp << "   temp    "  << sub << "  sub" << c<< "\n";
                    sub+=temp;
                }
                temp = sub;
                
//                 if(!str.empty()){
//                     string t=str.top();
//                     str.pop();
//                     temp=t+temp;
//                     str.push(temp);
//                     temp="";
//                 }
                
//                 cout<< temp<< "\n";
                
            }else{
                temp+=s[i];
            }
        }
        // if(!str.empty()){
        //     string t=str.top();
        //     str.pop();
        //     temp=t+temp;
        // }
        return temp;
    }
};