class Cat:
    def __init__(self, name, color='흰색'):
        self.name = name
        self.color = color

    def meow(self):
        print(f'내이름은 {self.name}, 색깔은 {self.color}, 야옹 야옹')


nabi = Cat("나비","흰섹")
nabi.meow()
nero = Cat("네로","검은색")
nero.meow()
mimi = Cat("미미","갈색")
mimi.meow()