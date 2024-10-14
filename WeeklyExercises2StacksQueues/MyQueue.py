class MyQueue(object):

    def __init__(self):
        self.leftStack = []
        self.rightStack = []
        
    def move_left(self):
        while len(self.rightStack) > 0:
            self.leftStack.append(self.rightStack.pop())
        
    def move_right(self):
        while len(self.leftStack) > 0:
            self.rightStack.append(self.leftStack.pop())

    def push(self, x):
        self.move_right()
        self.leftStack.append(x)
        self.move_left()
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        # self.move_right()
        # holder = self.rightStack.pop()
        # self.move_left()
        # return holder
        return self.leftStack.pop()
        """
        :rtype: int
        """
        

    def peek(self):
        # self.move_right()
        # holder = self.rightStack.pop()
        # self.rightStack.append(holder)
        # self.move_left()
        # return holder
        holder = self.leftStack.pop()
        self.leftStack.append(holder)
        return holder
        """
        :rtype: int
        """
        

    def empty(self): 
        return len(self.leftStack) == 0
        """
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


"""Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

Notes:

    You must use only standard operations of a stack, 
    which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, the stack may not be supported natively. 
    You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

 

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

 

Constraints:

    1 <= x <= 9
    At most 100 calls will be made to push, pop, peek, and empty.
    All the calls to pop and peek are valid.
"""


### testing 

print ("start")
myQueue = MyQueue();

print (    myQueue.push(1)) #// queue is: [1]
print(    myQueue.push(2)) #// queue is: [1, 2] (leftmost is front of the queue)
print(    myQueue.peek()) #// return 1
print (  myQueue.pop()) #// return 1, queue is [2]
print  (  myQueue.empty()) #// return false
    
print ("end")