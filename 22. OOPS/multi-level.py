class Grandparent:
    def __init__(self, grandparent_name):
        self.grandparent_name = grandparent_name

    def show_grandparent(self):
        return f"Grandparent: {self.grandparent_name}"


class Parent(Grandparent):
    def __init__(self, grandparent_name, parent_name):
        super().__init__(grandparent_name)
        self.parent_name = parent_name

    def show_parent(self):
        return f"Parent: {self.parent_name}"


class Child(Parent):
    def __init__(self, grandparent_name, parent_name, child_name):
        super().__init__(grandparent_name, parent_name)
        self.child_name = child_name

    # def __init__(self, grandparent_name, parent_name, child_name):
    #     Grandparent.__init__(self, grandparent_name)
    #     self.parent_name = parent_name
    #     self.child_name = child_name

    def show_child(self):
        return f"Child: {self.child_name}"


# Example usage
child = Child("John", "Michael", "David")
print(child.show_grandparent())  # Output: Grandparent: John
print(child.show_parent())  # Output: Parent: Michael
print(child.show_child())  # Output: Child: David
