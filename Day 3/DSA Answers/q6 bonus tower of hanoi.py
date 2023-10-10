'''
6.	(Bonus) Recursion Question: Tower of Hanoi (Total 20 points)
In this exercise, you will implement the Tower of Hanoi puzzle, recursively. The aim is to transfer all disks from one rod to the other. 
However, there are rules:
-	Only move one disk at a time.
-	Only take the upper disk from one of the stacks and place it on top of the other stack.
-	Cannot put a larger disk on top of a smaller one.
If you are good at imagining, here is an example of this: 
given the number of disks = 3, the sequence of disks traversing should happen:
 
Disk 1 moved from A to B
Disk 2 moved from A to C
Disk 1 moved from B to C
Disk 3 moved from A to B
Disk 1 moved from C to A
Disk 2 moved from C to B
Disk 1 moved from A to B

Hint: 
- notice the pattern of the disk number, we call it n. 
- To do a recursive function, these are called, executed and then resolved backwards, which is why you can see the base case, n = 1. 
- After n = 1, the previous unresolved case, n = 2, is called and resolved. 
- Then, moving on, it activated the base case again, then resolved the unresolved “previous-previous” case, n = 3. 
- Lastly, this cycle repeats itself, which is why you can see the intervals of the cycle being {1, 2, 1}, repeated twice. 

Implement the Tower of Hanoi where n = 3, and there are rods A, B, and C. (If you can go to n = 4, or above, why not? 😊)
'''

# Original recursion method:
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

# Example usage
print("Using original recursion method:")
tower_of_hanoi(3, 'A', 'C', 'B')


# Or, coding the movement of disks explicitly, and independently:
no_discs = 3
tower_a = []
tower_b = []
tower_c = []

for i in range(no_discs, 0, -1):
    tower_a.append(i)

print("\nUsing movements of disks, coded explicitly, and independently: ")
print("Initial state of towers:", tower_a, tower_b, tower_c)

def a_to_b(disc):
    tower_a.remove(disc)
    tower_b.append(disc)
def a_to_c(disc):
    tower_a.remove(disc)
    tower_c.append(disc)
    
def b_to_a(disc):
    tower_b.remove(disc)
    tower_a.append(disc)
def b_to_c(disc):
    tower_b.remove(disc)
    tower_c.append(disc)

def c_to_a(disc):
    tower_c.remove(disc)
    tower_a.append(disc)
def c_to_b(disc):
    tower_c.remove(disc)
    tower_b.append(disc)

def a_to_b_move_2(discs):
    a_to_c(discs[0])
    a_to_b(discs[1])
    c_to_b(discs[0])

def b_to_c_move_2(discs):
    b_to_a(discs[0])
    b_to_c(discs[1])
    a_to_c(discs[0])


a_to_b_move_2([1,2])
print("After moving disks 1 and 2, from A to C:", tower_a, tower_b, tower_c)
a_to_c(3)
print("After moving disk 3, from A to C", tower_a, tower_b, tower_c)
b_to_c_move_2([1,2])
print("After moving disks 1 and 2, from B to C:", tower_a, tower_b, tower_c)