# Eqileader

*PROBLEM:*

> A non-empty zero-indexed array A consisting of N integers is given
> 
> The leader of this array is the value that occurs in more than half of the elements of A.
> 
> An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.
> For example, given array A such that:
```
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
```    
we can find two equi leaders:
0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.


```c#
        public int Equileader(int[] A) {
            int n = A.Length;
            int size =0;
            Stack<int> s = new Stack<int>();
            
            // I like this piece of code. It doesn't push all element into the stack, instead, it only push the element that could 
            // be candidate.
            for (int i=0; i<n; i++)
            {
                if(size ==0)
                {
                    size +=1;
                    s.Push(A[i]);
                }
                else
                {
                    if (s.Peek() != A[i]) size -=1;
                    else size +=1;
                }           
            }
            int candidate = -1;
            if (size>0) candidate = s.Peek();
            int count =0;
            int leader= -1;
            
            for (int i=0; i<n; i++)
            {
            if (A[i] == candidate) count +=1;
            if (count > n/2) leader = candidate;
            }
            
            int equiLeaders=0;
            int leaders=0;
            
            //I also like this method. It is an obvious that the lead of the two slice must be the lead of the whole array.
            for (int i=0; i<n; i++)
            {
                if (A[i] == leader) leaders++;
                if (leaders >(i+1)/2 && count-leaders >(n-1-i)/2) equiLeaders++;             
            }        
            
            return equiLeaders;
        }

```
