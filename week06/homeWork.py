from tabulate import tabulate

class Node():
    def __init__(self, data:any) -> None:
        self.data = data
        self.next = None

class QLinkList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def enqueue(self, data:any) -> None:
        """just enqueue put new data to end of queue"""
        temp = Node(data)
        if self.head == None:
            self.head = temp
            self.tail = self.head
        else:
            self.tail.next = temp
            self.tail = self.tail.next
    
    def dequeue(self) -> any:
        """just dequeue return data in front of queue"""
        temp = self.head
        if self.head == None:
            print("Queue under flow")
            return
        elif self.head.next == None:
            self.head = None
            return temp.data
        else:
            self.head = self.head.next
            return temp.data
    
    def insert(self, data:any, where:int) -> None:
        """where mean what index of data you wanna put new data in front of it"""
        new = Node(data)
        if where > 0:
            current = self.head
            temp = current
            for _ in range(where):
                temp = current
                if current.next == None:
                    print("index out of range")
                else:
                    current = current.next
            temp.next = new
            new.next = current
        elif where == 0:
            temp = self.head
            self.head = new
            self.head.next = temp
        else:
            print("index should be >= 0")
    
    def update(self, data:any, where:int) -> None:
        """where mean what index of data you wanna update it"""
        if where > 0:
            temp = self.head
            for _ in range(where):
                temp = temp.next
            temp.data = data
        elif where == 0:
            self.head.data = data
        else:
            print("index should be >= 0")
    
    def delete(self, where:int) -> None:
        """where mean what index of data you wanna delete it"""
        if where > 0:
            current = self.head
            temp = current
            for _ in range(where):
                temp = current
                current = current.next
            temp.next = current.next
    
    def search(self, where:any) -> dict:
        """where mean what kind of data you wanna find it"""
        index = -1
        current = self.head
        if current != None:
            while current != None:
                index += 1
                print(current.data)
                if current.data == where:
                    return {'index':index, 'obj':current}
                current = current.next
        print("can't match data ("+str(where)+") in queue")
    
    def displayQ(self) -> None:
        """show all data in queue"""
        if self.head != None:
            table_data = [['Index', 'Value']]
            current = self.head
            index = -1
            while current != None:
                index += 1
                table_data.append([index, current.data])
                current = current.next
            print(tabulate(table_data, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print("Queue is empty")

queue = QLinkList()
main_menu = ["1.enqueue", "2.dequeue", "3.insert queue", "4.delete queue", "5.update data in queue", "6.display all data in queue", "7.exit"]

while True:
    print("\nSelect menu")
    print('   ' + '\n   '.join(main_menu))
    try:
        selected_op = int(input("Input number of menu : "))
    except:
        print("Pls input number!")
        continue
    
    if selected_op in [1, 2, 3, 4, 5, 6, 7]:
        if selected_op == 1:
            print("\nEnqueue selected")
            while True:
                data = input("Enqueue, Input data sep by comma(1,2,3,4,5) or 'e' for back to main menu : ")
                if data == "e" or data == "E":
                    break
                data = data.split(",")
                for i in data:
                    queue.enqueue(data=i)
                print("Enqueue success")
                queue.displayQ()
        
        elif selected_op == 2:
            print("\nDequeue selected")
            tmp_q = queue.dequeue()
            if tmp_q != None:
                print("result is", tmp_q)
        
        elif selected_op == 3:
            print("\nInsert queue selected")
            if queue.head != None:
                while True:
                    queue.displayQ()
                    print("Insert queue, Shoose index what you wanna put new data in front of it")
                    new_data = input("Input index and new data sep by comma(1,'cat') or 'e' for back to main menu : ")
                    if new_data == "e" or new_data == "E":
                        break
                    new_data = new_data.split(",")
                    try:
                        new_data[0] = int(new_data[0])
                        queue.insert(data=new_data[1], where=new_data[0])
                    except:
                        print("Input worng format")
                        continue
            else:
                print("Queue is empty pls enqueue first")
        
        elif selected_op == 4:
            print("\nDelete queue selected")
            if queue.head != None:
                while True:
                    queue.displayQ()
                    print("Delete queue, Shoose index what you wanna delete it")
                    index = input("Input index or 'e' for back to main menu : ")
                    if index == 'e' or index == 'E':
                        break
                    try:
                        index = int(index)
                        queue.delete(index)
                        print("Queue deleted")
                    except:
                        print("Input wrong format")
                        continue
            else:
                print("Queue is empty pls enqueue first")
        
        elif selected_op == 5:
            print("\nUpdate data Selected")
            if queue.head != None:
                while True:
                    queue.displayQ()
                    print("Update data, Shoose index what you wanna update it")
                    new_data = input("Input index and new data sep by comma(1,'cat') or 'e' for back to main menu :  : ")
                    if new_data == 'e' or new_data == 'E':
                        break
                    new_data = new_data.split(",")
                    try:
                        new_data[0] = int(new_data[0])
                        queue.update(new_data[1], new_data[0])
                        print("data updated")
                    except:
                        print("Input wrong format")
                        continue
            else:
                print("Queue is empty pls enqueue first")
        
        elif selected_op == 6:
            print("\nDisplay all data selected")
            if queue.head != None:
                queue.displayQ()
            else:
                print("Queue is empty pls enqueue first")
        
        elif selected_op == 7:
            break
    else:
        print("Menu out of range pls input 1-7")
        continue

# test case
    # menu 1
    # menu 2
    # menu 3
    # menu 4
    # menu 5
    # menu 6
    # menu 7