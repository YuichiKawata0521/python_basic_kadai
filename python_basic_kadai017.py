class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name} は大人です")
        else:
            print(f"{self.name} は大人ではありません")

# Humanクラスのインスタンスを生成してリストに追加
humans = [
    Human("Greed", 25),
    Human("Gluttony", 40),
    Human("Lust", 18),
    Human("Wrath", 56),
    Human("Sloth", 70),
    Human("Pride", 5),
    Human("Envy", 21)
]

# リストの要素数分だけcheck_adultメソッドを呼び出す
for human in humans:
    human.check_adult()
