class Person:
    def __init__(self, n, a):
        self._name = n
        self.__age = a

    def get_age(self):
        return self.__age

    def introduce(self):
        return "Hello, I am " + self._name + " and I am " + str(self.__age) + " years old."

class Student(Person):
    def __init__(self, n, a, sid):
        super().__init__(n, a)
        self.student_id = sid

    def introduce(self):
        return "Hi, I'm student " + self._name + " (ID: " + self.student_id + "). I am " + str(self.get_age()) + " years old."

def greet_person(p):
    print(p.introduce())

if __name__ == "__main__":
    p = Person("John Doe", 30)
    s = Student("Jane Smith", 20, "S12345")

    print("--- Encapsulation Check ---")
    try:
        print(p.__age)
    except:
        print("Cannot access private attribute '__age' directly.")
    print("Accessing age via getter: " + str(p.get_age()))

    print("\n--- Polymorphism Demonstration ---")
    greet_person(p)
    greet_person(s)
