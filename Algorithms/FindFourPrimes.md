# Find four primes

Recently I was looking for a job. Most companies send a paper test before on-site interview.

Last month, I received a test as below:

> I have four different prime number all under 1000. I have noticed that the product of these primes is a twelve-digit number whose digits are either sequential or the same as previous one.
>
>What are the four digits?

``` c#

 public int[] FindFourPrimes(int N)  {
            var primes = Primes(N);
            var lstPrimes = new List<int>();
            for(var i = 0; i < N; i++) {
                if(primes[i]) {
                    lstPrimes.Add(i);
                }
            }

            for(var a = 0; a < lstPrimes.Count(); a++) {
                for(var b = a+1; b < lstPrimes.Count(); b++) {
                    for(var c = b+1; c < lstPrimes.Count(); c++) {
                        for(var d = c+1; d < lstPrimes.Count(); d++) {
                            if(IsSeqInt(lstPrimes[a]*lstPrimes[b] * lstPrimes[c] *lstPrimes[d])) {
                                return new int[] {lstPrimes[a],lstPrimes[b],lstPrimes[c],lstPrimes[d]};
                            }
                        }
                    }
                }
            }

            return null;
        }

        public bool IsSeqInt(int n)
        {
            var str = n.ToString();
            if(str.Length != 12) return false;

            for(var i = 0; i < str.Length-1; i++) {
                if(str[i] != str[i+1] && Math.Abs(str[i]-str[i+1]) != 1) {
                    return false;
                }
            }

            return true;
        }

        public bool[] Primes(int N)
        {
            var ret = new bool[N+1];
            for(int i = 2; i < N+1; i++)
            {
                ret[i] = true;
            }
            for(int i = 2; i*i <= N; i++)
            {
                if(ret[i])
                {
                    var ite = i * 2;
                    while(ite < N+1)
                    {
                        ret[ite] = false;
                        ite += i;
                    }
                }
            }

            return ret;
        }
```

The result is null!