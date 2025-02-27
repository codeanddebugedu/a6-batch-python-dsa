class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def show_father(self):
        print(f"Father: {self.father_name}")


class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

    def show_mother(self):
        print(f"Mother: {self.mother_name}")


class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)  # Call init of specific class
        Mother.__init__(self, mother_name)  # Call init of specific class
        self.child_name = child_name

    def show_child(self):
        print(f"Child: {self.child_name}")


# Example usage
child = Child("John", "Jane", "Alice")
child.show_father()
child.show_mother()
child.show_child()
