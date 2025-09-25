class Animal:
    def speak(self):
        print("動物が鳴きます")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("ワンワン!")
        

def main():
    # a = Animal()
    # a.speak()

    d = Dog()
    d.speak()
    

if __name__ == "__main__":
    main()