class Animal:
    def __init__(self, name):
        self.name = name  # Tên động vật

    def sound(self):
        """Phương thức sound chưa được định nghĩa, sẽ được ghi đè trong lớp con."""
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  # Khai báo tên sử dụng super

    def sound(self):
        """Ghi đè phương thức sound để in ra tiếng kêu của chó."""
        print(f"{self.name} nói: Gâu Gâu!")

# Ví dụ sử dụng lớp Dog
dog = Dog("Buddy")
dog.sound()  # In ra tiếng kêu của chó