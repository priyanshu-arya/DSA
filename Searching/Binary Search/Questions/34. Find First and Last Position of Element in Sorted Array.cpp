// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#include<iostream>
#include<stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l = BinarySearchrecursive(nums, target, 0, nums.size()-1);
        int r = BinarySearchrecursive(nums, target, 0, nums.size()-1);
        return {l, r};
    }

private:
    int BinarySearchrecursive(vector<int>& nums, int target, int low, int high) {
        if(low > high)
            return -1;
        
        int mid = low + (high-low)/2;
        
        if(target == nums[mid])
            return mid;
        else if(nums[mid] > target)
            return BinarySearchrecursive(nums, target, low, mid-1);
        return BinarySearchrecursive(nums, target, mid + 1, high); 
    }
};