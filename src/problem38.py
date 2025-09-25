class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"名前: {self.name}, 年齢: {self.age}"
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def greet(self):
        print(f"こんにちは、{self.name}です")


def main():
    person = Person("太郎", 20)
    person.greet()
    

if __name__ == "__main__":
    main()