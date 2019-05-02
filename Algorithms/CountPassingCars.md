# Count passing cars

It is an easy question from Codility under part of 'Prefix Sum'.

In the question, *passing cars* means the cars pass with each other. So given array {0, 1, 0, 1, 1} will be demostrated as 

    0   1   2   3   4
    ->      ->
        <-      <-  <-
So, (0,1)   (0,3)   (0,4)   (2,3)   (2,4) will meet with each other.

Below is my solution which is not perfect as it needs travel two times of the array.

``` c#
public int CountPassingCars(int[] A) {
    var nums = 0;
    var eastCars = 0;
    foreach(var a in A) {
        eastCars += a;
    }
    foreach(var a in A) {
        if(a == 0) {
            nums += eastCars;
        } else {
            eastCars -= 1;
        }
    }
    return nums > 1000000000 ? -1 : nums;
}
```

Below is a better solution:

``` c#
public int CountPassingCars2(int[] A)
{
    int count = 0;
    int multiply = 0;
    foreach (int car in A)
    {
        if (car == 0)
        {
            multiply = multiply + 1;
        }
        if (multiply > 0)
        {
            if (car == 1)
            {
                count = count + multiply;
                if (count > 1000000000)
                {
                    return -1;
                }
            }
        }
    }
    return count;
}
```