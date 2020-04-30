class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.fiu_stanga = None
        self.fiu_dreapta = None


class splaytree:
    def __init__(self):
        self.root = None

    def insert(self, nr):
        node = Node(nr)
        y = None
        x = self.root

        while x != None:
            y = x
            if node.val < x.val:
                x = x.fiu_stanga
            else:
                x = x.fiu_dreapta

        node.parent = y
        if y == None:
            self.root = node
        elif node.val < y.val:
            y.fiu_stanga = node
        else:
            y.fiu_dreapta = node
        self.splay(node)

    def find_function(self, node, nr):
        if node == None or nr == node.val:
            return node

        if nr < node.val:
            return self.find_function(node.fiu_stanga, nr)
        return self.find_function(node.fiu_dreapta, nr)

    def find_node(self, k):
        x = self.find_function(self.root, k)
        if x != None:
            self.splay(x)
            return x
        else:
            return None

    def find(self,x):
        if self.find_node(x):
            g.write(str(1)+"\n")

        else:
            g.write(str(0)+"\n")


    def DELETE(self, node, nr):
        x = None
        tree1 = None
        tree2 = None
        while node != None:
            if node.val == nr:
                x = node

            if node.val <= nr:
                node = node.fiu_dreapta
            else:
                node = node.fiu_stanga

        self.splay(x)
        if x.fiu_dreapta != None:
            tree1 = x.fiu_dreapta
            tree1.parent = None
        else:
            tree1 = None

        tree2 = x
        tree2.fiu_dreapta = None
        x = None

        if tree2.fiu_stanga != None:
            tree2.fiu_stanga.parent = None

        self.root = self.join(tree2.fiu_stanga, tree1)
        tree2 = None

    def delete(self, val):
        self.DELETE(self.root, val)

    def rotire_stanga(self, x):
        y = x.fiu_dreapta
        x.fiu_dreapta = y.fiu_stanga
        if y.fiu_stanga != None:
            y.fiu_stanga.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.fiu_stanga:
            x.parent.fiu_stanga = y
        else:
            x.parent.fiu_dreapta = y
        y.fiu_stanga = x
        x.parent = y

    def rotire_dreapta(self, x):
        y = x.fiu_stanga
        x.fiu_stanga = y.fiu_dreapta
        if y.fiu_dreapta != None:
            y.fiu_dreapta.parent = x

        y.parent = x.parent;
        if x.parent == None:
            self.root = y
        elif x == x.parent.fiu_dreapta:
            x.parent.fiu_dreapta = y
        else:
            x.parent.fiu_stanga = y

        y.fiu_dreapta = x
        x.parent = y

    def splay(self, x):
        while x.parent != None:
            if x.parent.parent == None:
                if x == x.parent.fiu_stanga:
                    self.rotire_dreapta(x.parent)
                else:
                    self.rotire_stanga(x.parent)
            elif x == x.parent.fiu_stanga and x.parent == x.parent.parent.fiu_stanga:
                self.rotire_dreapta(x.parent.parent)
                self.rotire_dreapta(x.parent)
            elif x == x.parent.fiu_dreapta and x.parent == x.parent.parent.fiu_dreapta:
                self.rotire_stanga(x.parent.parent)
                self.rotire_stanga(x.parent)
            elif x == x.parent.fiu_dreapta and x.parent == x.parent.parent.fiu_stanga:
                self.rotire_stanga(x.parent)
                self.rotire_dreapta(x.parent)
            else:
                self.rotire_dreapta(x.parent)
                self.rotire_stanga(x.parent)

    def maximum(self, node):
        while node.fiu_dreapta != None:
            node = node.fiu_dreapta
        return node

    def join(self, tree1, tree2):
        if tree1 == None:
            return tree2

        if tree2 == None:
            return tree1

        x = self.maximum(tree1)
        self.splay(x)
        x.fiu_dreapta = tree2
        tree2.parent = x
        return x

    def afisare(self, node):
        if node != None:
            print(node.val,end=" ")
            self.afisare(node.fiu_stanga)
            self.afisare(node.fiu_dreapta)

    def preorder(self):
        self.afisare(self.root)
        print("")

    def succesor(self, x):
        while self.find_node(x) == None:
            x+=1
            if x>1000001:
                return -1
        return self.find_node(x).val

    def predecesor(self, x):
        while self.find_node(x) == None:
            x-=1
            if x<-1000001:#merge si pt -1.000.000.000 dar se misca greu
                return -1
        return self.find_node(x).val

    def sort(self,x,y):
        for i in range(x+1,y):
            if self.find_node(i) != None:
                g.write(str(i) + " ")
        g.write("\n")






f=open("date.in","r")
g=open("date.out","w")
N=int(f.readline())
ok=int(N)
T=splaytree()
#comanda 1: insert
#comanda 2: delete
#comanda 3: search
#comanda 4: succesor
#comanda 5: predecesor
#comanda 6: sortare 
while(ok):
    s=f.readline()
    ss = s.split()
    if int(ss[0]) == 1:
        T.insert(int(ss[1]))
    if int(ss[0]) == 2:
        T.delete(int(ss[1]))
    if int(ss[0]) == 3:
       T.find(int(ss[1]))
    if int(ss[0]) == 4:
        g.write(str(T.succesor(int(ss[1]))) + "\n")

    if int(ss[0]) == 5:

        g.write(str(T.predecesor(int(ss[1]))) + "\n")
    if int(ss[0]) == 6:
            T.sort(int(ss[1]), int(ss[2]))
    ok=ok-1
f.close()
g.close()