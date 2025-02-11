# Parameters vs Arguments
def addition(a: int, b: int):
    total = a + b
    print(total)


def greeting(name: str, age: int, gender: str):
    print(f"Hi {name}, you are {age} years old and you are a {gender}")


addition(5, 10)
# addition("Anirudh", "Khurana")
# addition(5.5, 8.1)
greeting("Anirudh", 44, "Male")
