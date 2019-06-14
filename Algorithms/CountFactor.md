# CountFact  

What I learnt from this test is **multiplication method** is a time consuming operation in C#.

The question is as below:

> A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.
> 
> For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).
>
> Write a function:
>
> ``` c#
> class Solution { public int solution(int N); }
> ```
>
> that, given a positive integer N, returns the number of its factors.
>
> For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

The code below is getting expired error with large input:
```c#
        public int CountFactor(int N) {
            var count = 0;
            var i = 1;

            while(i * i < N) {
                if(N % i == 0) count += 2;
                i++;
            }

            if(i*i == N) count++;

            return count;
        }
```

The improvment is calculating upbound of i before while:
```c#
        public int CountFactor_improve(int N) {
            var count = 0;
            var upBound = Convert.ToInt32(Math.Sqrt(N));
            for(var i = 1; i <= upBound; i++) {
                if(N%i == 0) count += 2;
            }
            if(upBound * upBound == N) count--;

            return count;
        }
```
