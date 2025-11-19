Data Structures and Algorithms

DS (array, string, linked list, stack, queue,tree, graph)

A(searching, sorting, divide&conquer, hashing, greedy, recursion, backtracking, tree&graphtraversal, dynamic programming)

- Different data structures are optimised for different scenarios

- Big O (speed and efficiency) are of 4 types
  O(1) -> the fastest an algo. can operate irrespective of input data (e.g. if the operation takes same time to pick one fruit or 1000 fruits or more)
  The Big O notation graph is based on time required vs size of input data (n)

  O(n) -> linear time -> as the amount of data increases, the time to complete the operation increases. Still good.

  O(n^2) -> the slowest nightmare

  O(log n) -> the hidden shortcut (e.g. in dictionary, we go to the middle of the book and check whether the word that we want to look for comes before or after. Depending on that we move forward or backward. This process is repeated until we find the word) (time -> half, then half of that, and so on)

  * Array
  - store data in a continuous manner, i.e., all elements are placed side-by-side in memory. Bcoz each elements have specific index, retrieving a value is extremely fast (e.g., arr[2] = 3) as we can directly go to the position without searching. But adding elements in between is difficult. 

  In terms of time complexity, accessing any element by its index is O(1) operation, and hence it is super efficient. Inserting an element is also O(1), if you are simply replacing an existing item. But inserting an item beyond the array size requires copying the whole array, and then adding, which requires O(n) time complexity

  Deleting an element is also O(n), bcoz once an element is deleted, all subsequent elements will shift forwards, to maintain continuous structure of array, unless deleting at the very end of the array (O(1)).


  * Linked List (like a train)
   - Need to move thru each cart starting from front until you reach the required card.

   - Each element is stored in a separate node, and each node contain separate value and a pointer to the next node in the sequence. This makes linked list more flexible than arrays as we can easily add or remove elements without worrying about shifting everything around. However, accessing a specific element is slower as you have traverse from the beginning to find it.

   - Time complexity to access an element -> O(n)

   - Time complexity to insert an element or to delete an element -> O(1)


   * Stack (LIFO, like pringles)
   - Accessing or seraching time complexity -> O(n) operation
   - inserting an element or deleting an element -> O(1) operation


   * Queue (FIFO, like in billing after shopping)
   - Elements are added only in the back and removed from the front
   - Big O complexity here, just like stack, cannot access or search elements elements by index, hence O(n) operation
   - Insertion and deletion -> O(1) operation, 
   i.e., simply add to the back and remove from the front


   * Heap(Priority Queue)
   - Think of it like a pyramid of stacked boxes, where the smallest box is always at the very top. So, if we remove any box from the box, they need to readjust to maintain its pyramid structure. 

   Two types of heap (min heap and max heap)

   - Min heap, where every parent is smaller than their children (top element is the smallest).

   - Max heap, where every parent is larger than than their children (top element is the largest)

   - Time complexity to access the top element is 
   O(1), while for any other arbitrary element, it is O(n)

   - Time complexity to insert an element is 
   O(log(n)) operation (bcoz of heap property of parent-child relation being bigger or smaller, it bubbles up or down)

   Similarly, removing an element is also O(log n), as it removes the element (only the root element), and then bubbles around to restore the heap property

   * Hashmap
   - stores data using key-value pairs (key runs thru a hash function which determines where the value to be stored)
   - needs hash collision resolution which could be a linked list chaining from the hashmap position, or it could be a linear probing where we find the next available position. This is the only downside of hashmap

   - accesing an element by its key in hashmap -> O(1), but worse case, O(n), if everything is put on to that linked list

   - deleting an element is also O(1), but for linked list from that postion, its O(n) operation.

  - In python, hashmaps are pretty much same as dictionary


  * Binary search tree
  - similar to family tree, but key difference is that each node follows a specific ordering rule, the left child must have values lower than the parent, the right child must have values greater than the parent. This makes searching, insertion and deletion extremely efficient.

  - accessing, inserting and deleting -> O(log n)

  - but if the binary search tree is unbalanced for some reason, it will look like a linked list, and hence accessing, inserting and deleting takes 
  O(n) operation.


  * Set
  - An unordered collection of unique elements typically implemented using a hash table

  - inserting/ deleting -> O(1) operation, but worse case scenario, it can be O(n) for hash set?

Arrays/LinkedLists/Stacks/Queues/Binary Trees/Hash Tables