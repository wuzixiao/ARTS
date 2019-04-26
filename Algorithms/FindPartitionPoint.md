# Find a partition point

This is an another question I got in the interview recently. 

> Given an unsorted array of integers. Find an element such that all the elements to its left are smaller and to its right are greater. Print -1 if no such element exists.

Example:

>Input :  A[] = {4, 3, 2, 5, 8, 6, 7}
>
>Input : A[] = {5, 6, 2, 8, 10, 9, 8} 
>
>Output : -1

There are several solutions to resolve this problem:
1. Iterate from the left side of the list, say i is current point. get the max of i's left. Use it compare with the right of i, if no element is smaller than i. It is the position.
2. Obviously, the 1st solution is too slow because it is O(n*n). It can be optimized by using O(n) space to save the largest temperature of right of each element thus we don't need to iterate the inner loop.

``` c#
public int FindChangePoint_Better(int[] T) {
    var maxLeft = Int32.MinValue;
    var minRight = Int32.MaxValue;
    var len = T.Length;
    var minsRight = new int[len];
    //build minsRight array from right to left
    for(var i = T.Length-1; i >= 0; i--) {
        minsRight[i] = Math.Min(minsRight[i], minRight);
        minRight = minsRight[i];
    }

    for(var i = 0; i < T.Length -1; i++) {
        maxLeft = Math.Max(T[i], maxLeft);
        if(maxLeft == minsRight[i]) {
            return i;
        }
    }

    return -1;
}
public int FindChangePoint(int[] T) 
{
    var maxLeft = Int32.MinValue;
    var minRight = Int32.MaxValue;

    for(var i = 0; i < T.Length-1; i++) {
        maxLeft = Math.Max(maxLeft, T[i]);
        for(var j = i + 1; j < T.Length; j++) {
            minRight = Math.Min(minRight, T[j]);
            if(minRight > maxLeft) {
                return i;
            }
        }
    }

    return -1; //no solution
}
```