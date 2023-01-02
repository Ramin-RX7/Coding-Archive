from dataclasses import dataclass

@dataclass
class Node:
    data : None = None
    next : None = None

    def __repr__(self) -> str:
        return f"Node({self.data})"


class LinkedList:
    def __init__(self) -> None:
        self.head : Node|None  = None
        self.size = 0


    def __str__(self) -> str:
        if self.is_empty():  return ""

        iterate = self.head
        item_list: list[str] = []
        while iterate:
            item_list.append(str(iterate.data))
            iterate = iterate.next
        return  " --> ".join(item_list)


    def is_empty(self) -> bool:
        return self.head is None


    def append(self, new):
        if self.is_empty():
            self.head = new
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new
        self.size += 1


    def pop(self):
        if not self.is_empty():
            last = self.head
            while last.next.next:
                last = last.next
            ret = last.next
            last.next = None
            self.size -= 1
            return ret

    def search(self,item):
        if not self.is_empty():
            last = self.head
            while last:
                if last == item:  # or we can search the data with last.data
                    return True
                last = last.next
            



rx.cls()

Nodes_List = []
for name in ["Ramin","Ali","Mahdi","Kourosh","Moein"]:
    new = Node()
    new.data = name
    Nodes_List.append(new)
print(f"Nodes List:  {Nodes_List}")


print("")


MyLL = LinkedList()


print("ADD (and Print):")
for node in Nodes_List:
    MyLL.append(node)
    print(MyLL)

print()

print("PRINT:")
print(MyLL)

print()

print("POP:")
for i in range(3):
    print(f"Popped: {MyLL.pop()}")
    print(f"    {MyLL}")

print()
print(MyLL)
print()

print("SEARCH:")

for node in Nodes_List:
    print(f"Searching for {node}:  ",end="")
    print(MyLL.search(node))
print()
