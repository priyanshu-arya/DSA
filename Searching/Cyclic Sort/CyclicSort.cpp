#include <bits/stdc++.h>
#include<iostream>

using namespace std;

class Solution{
    public:
    void swap(vector<int> arr, int i, int correct){
        int temp = arr[i];
        arr[i] = arr[correct];
        arr[correct] = temp;
    }
    void sort(vector<int> nums){
        int i = 0;
        while (i < nums.size()){
            int correct = nums[i] - 1;
            if (nums[i] != nums[correct]) swap(nums, i, correct);
            else i++;
        }
    }
};

 main(){
    Solution s;
    vector<int> arr = {4, 5, 2, 3, 1};
    s.sort(arr);
    
    for(int i = 0; i < arr.size(); i++) cout<< arr[i] << " ";
}