'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack:  # it is passed , but not O(1)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []

    def push(self, x: int) -> None:
        if self.min is not None:
            self.min = min(x, self.min)
        else:
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        m = self.stack.pop()
        if m == self.min:
            s = sorted(self.stack)
            if len(s) == 0 :
                self.min = None
            else:
                self.min = s[0]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        

# Hint : consider each node in the stack has a min
class MinStack2: 
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        if self.min is None:
            self.min = x
        else:
            self.min = min(x, self.min)

        self.stack.append((x, self.min))
    
    def pop(self) -> None:
        t = self.stack.pop()
        if len(self.stack) == 0:
            self.min = None
        else:
            self.min = self.stack[-1][1]
    
    def top(self) -> int:
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.min
