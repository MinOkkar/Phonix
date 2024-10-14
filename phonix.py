# title 

print("-----------------------------------------------------------------------")
print("|         ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗██╗██╗  ██╗              |")
print("|         ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██║╚██╗██╔╝              |")
print("|         ██████╔╝███████║██║   ██║██╔██╗ ██║██║ ╚███╔╝               |")
print("|         ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██║ ██╔██╗               |")
print("|         ██║     ██║  ██║╚██████╔╝██║ ╚████║██║██╔╝ ██╗              |")
print("|         ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝              |")
print("| Phone Book Management System using Binary Search Tree (BST)         |")
print("| by CS students - DSA course - 2024                                  |")
print("-----------------------------------------------------------------------")

# tile 

#BST
class Node:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.left = None
        self.right = None

class PhoneBook:
    def __init__(self):
        self.root = None

    def insert(self, name, phone, email):
        phone = str(phone).strip()
        if self.root is None:
            self.root = Node(name, phone, email)
        else:
            self._insert_rec(self.root, name, phone, email)

    def _insert_rec(self, node, name, phone, email):
        #sort by name
        if name < node.name:
            if node.left is None:
                node.left = Node(name, phone, email)
            else:
                self._insert_rec(node.left, name, phone, email)
        else:
            if node.right is None:
                node.right = Node(name, phone, email)
            else:
                self._insert_rec(node.right, name, phone, email)

    def search(self, name):
        return self._search_rec(self.root, name)

    def _search_rec(self, node, name):
        if node is None:
            print(f"Username: {name} not found")
            return None
        if node.name == name:
            print(f"Found: Name: {node.name}, Phone: {node.phone}, Email: {node.email}")
            return node
        elif name < node.name:
            return self._search_rec(node.left, name)
        else:
            return self._search_rec(node.right, name)
        
    def search_by_phone(self, phone):
        phone = str(phone).strip()
        return self._search_by_phone_rec(self.root, phone)

    def _search_by_phone_rec(self, node, phone):
        if node is None:
            print(f"Phone number: {phone} not found.")
            return None
        if node.phone == phone:
            print(f"Found: Name: {node.name}, Phone: {node.phone}, Email: {node.email}")
            return node
        elif phone < node.phone:
            return self._search_by_phone_rec(node.left, phone)
        else:
            return self._search_by_phone_rec(node.right, phone)

    def search_by_email(self, email):
        return self._search_by_email_rec(self.root, email)

    def _search_by_email_rec(self, node, email):
        if node is None:
            print(f"Email: {email} not found.")
            return None
        if node.email == email:
            print(f"Found: Name: {node.name}, Phone: {node.phone}, Email: {node.email}")
            return node
        elif email < node.email:
            return self._search_by_email_rec(node.left, email)
        else:
            return self._search_by_email_rec(node.right, email)
        

    def update(self, name, new_phone=None, new_email=None):
        entry = self.search(name)
        if entry:
            if new_phone:
                entry.phone = new_phone
            if new_email:
                entry.email = new_email
            print(f"User: {name} updated successfully")
        else:
            print(f"{name} Not Available for Update.")

    def delete(self, name):
        if self.search(name):
            self.root = self._delete_rec(self.root, name)
            print(f"{name} deleted successfully")
        else:
            print(f"{name} does not exist")

    def _delete_rec(self, node, name):
        if node is None:
            return node

        if name < node.name:
            node.left = self._delete_rec(node.left, name)
        elif name > node.name:
            node.right = self._delete_rec(node.right, name)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor
            min_larger_node = self._min_value_node(node.right)
            node.name = min_larger_node.name
            node.phone = min_larger_node.phone
            node.email = min_larger_node.email
            node.right = self._delete_rec(node.right, min_larger_node.name)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def display(self):
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node:
            self._in_order_traversal(node.left)
            print(f"Name: {node.name}, Phone: {node.phone}, Email: {node.email}")
            self._in_order_traversal(node.right)

phone_book = PhoneBook()
phone_book.insert("Alice", "1234567890", "alice@example.com")
phone_book.insert("Bob", "9876543210", "bob@example.com")
phone_book.insert("Charlie", "5556667777", "charlie@example.com")



#BST


#login and terminal inputs
usr=input("Enter User Name : ")
pwd=input("Enter Password : ")
if usr == "admin" and pwd == "admin":
    print()
    print("-Login success")
    while True:
        print()
        print("1. Add new contact") #done
        print("2. Search contact") 
        print("3. Delete a contact") #done
        print("4. Update a existing contacts")
        print("5. Display all contacts")
        print("6. Exit the program")
        print()
        num = input("Please Enter ur choice: ")
        if num == "1":
            print()
            name = input("Please Insert Name : ")
            number = input("Please Insert Phone Number : ").strip()
            email = input("Please Insert Email : ")
            phone_book.insert(name,str(number),email)
            print("-new contact added succuesfully")
            print()
            continue



        if num == "2":
            while True:
                print()
                print("1. Search by Name")
                print("2. Search by phone number")
                print("3. Search by email")
                print()
                searchtype = input("Enter your Search Type: ")
                if searchtype == "1":
                    a1 = input("Search(Name): ")
                    phone_book.search(a1)
                    input("Press Enter to continue:")
                    break
                if searchtype == "2":
                    a2 = input("Search(Ph.no): ").strip()
                    phone_book.search_by_phone(str(a2))
                    input("Press Enter to continue:")
                    break
                if searchtype == "3":
                    a3 = input("Search(email): ")
                    phone_book.search_by_email(a3)
                    input("Press Enter to continue:")
                    break
                else: 
                    print("wrong input, try again")
                    continue

            continue

        if num == "3":
            n = input("Please Enter the contact Name to delete: ")
            phone_book.delete(n)
            print() 
            continue
        
        if num == "4":
            print()
            n1 = input("Enter the contact Name to update: ")
            print("-----please leave blank for no changes------")
            n2 = str(input(f"{n1} : new phone number: "))
            n3 = input(f"{n1} : new email: ")
            phone_book.update(n1,n2,n3)
            continue


        if num == "5":
            print()
            print("-----displaying all contacts-----")
            phone_book.display()
            print()
            input("Press Enter to continue:")



        if num == "6":
            print()
            yno=input("-Do you really want to exit the program? y/n :")
            if yno =="y":
                break
            elif yno =="n":
                continue
            else:
                continue
        else:
            print()
            print("please enter valid number(1,2,3,4,5,5)")
            continue





else : 
    print()
    print("-Error: Incorrect password or username")
    print()
    print("-Exiting the program")
    print()