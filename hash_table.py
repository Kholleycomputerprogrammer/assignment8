class Contact:
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key: str) -> int:
        # Simple hash: sum of ASCII values mod table size
        return sum(ord(char) for char in key) % self.size

    def insert(self, key: str, number: str):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)

        if self.data[index] is None:
            self.data[index] = new_node
        else:
            current = self.data[index]
            while current:
                if current.key == key:
                    current.value.number = number
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def search(self, key: str):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            if self.data[i] is None:
                print("Empty")
            else:
                current = self.data[i]
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


#TESTING
if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()

    print("\n--- Adding values ---")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\n--- Search for John ---")
    contact = table.search("John")
    print("Search result:", contact)

    print("\n--- Collision test ---")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.print_table()

    print("\n--- Duplicate key update ---")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    print("\n--- Search for missing contact ---")
    print(table.search("Chris"))  
 
