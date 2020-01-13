# Brackets  

It is a simple task to check if the brackets are properly nested.

> * S is empty;
> * S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
> * S has the form "VW" where V and W are properly nested strings.

using a stack solves this quesiton easily.

```c#
        public bool Brackets(string S) {
            var stack = new Stack<char>();
            Func<char, char, bool> pair = (c1, c2) =>
            {
                if(c1 == '(' && c2 == ')' || c1  == '[' && c2 == ']' || c1 == '{' && c2 == '}') {
                    return true;
                }
                return false;
            };

            for(var i = 0; i < S.Length; i++) {
                if(stack.Count == 0 || !pair(stack.Peek(), S[i])) {
                    stack.Push(S[i]);
                }else {
                    stack.Pop();
                }
            }

            return stack.Count == 0;
        }

```
