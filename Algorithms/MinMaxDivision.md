# MinMaxDivision

> You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.
> 
> You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.
> 
> The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.
> 
> The large sum is the maximal sum of any block.
> 
> For example, you are given integers K = 3, M = 5 and array A such that:
> 
  > A[0] = 2
  > A[1] = 1
  > A[2] = 5
  > A[3] = 1
  > A[4] = 2
  > A[5] = 2
  > A[6] = 2
> The array can be divided, for example, into the following blocks:
> 
> [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
> [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
> [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
> [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
> You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.
> 
> You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.
> 
> The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.
> 
> The large sum is the maximal sum of any block.
> 
> For example, you are given integers K = 3, M = 5 and array A such that:
> 
  > A[0] = 2
  > A[1] = 1
  > A[2] = 5
  > A[3] = 1
  > A[4] = 2
  > A[5] = 2
  > A[6] = 2
> The array can be divided, for example, into the following blocks:
> 
> [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
> [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
> [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
> [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
> The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

I've been thinkg this problem for a couple of days without a good solution. I thought there should be a way to divide the array with the min of max sum of subarray. 

Actually, the solution is to try with a number which is between A.Sum() and A.Max() to test the condition. If the condition is satisfied，trying with a smaller one until the min found.

* Code *

```c#
        private int getBlocks(int[] A, int mid)
        {
            var blocks = 1;
            var curSum = 0;
            foreach(var a in A)
            {
                if(curSum+a > mid)
                {
                    blocks += 1;
                    curSum = a; //the first element of next block is a
                }
                else
                {
                    curSum += a;
                }
            }

            return blocks;
        }

        public int MinMaxDivision(int K, int M, int[] A)
        {
            int max = A.Sum();
            int min = A.Max();
            while (min < max)
            {
                var mid = (min + max) / 2;
                var blocks = getBlocks(A, mid);
                if (blocks > K)
                {
                    min = mid+1;
                }
                else 
                { 
                    max = mid;
                }
            }

            return min;
        }
    }
```
