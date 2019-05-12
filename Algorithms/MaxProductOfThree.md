# MaxProductOfThree

It is a simple task of sorting on Codility online lesson. 

> A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

I used Array.Sort to sort the array firstly. Then get the largest 3 elements or the largest 1 element and the smallest 2 elements.
Because the smallest 2 could be nagetive number.

```c#
  public int MaxProductOfThree(int[] A) {
      Array.Sort(A);
      int len = A.Length;
      var prod1 = A[len-1] * A[len-2] * A[len-3];
      var prod2 = A[len-1] * A[0] * A[1];

      return Math.Max(prod1, prod2);
  }
```

An interesting follow question could be how to find the max product of N?
