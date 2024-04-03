import random
import string


class Robot:
    def __init__(self):
        s = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        d = ''.join(random.choice(string.digits) for _ in range(3))
        self.name = s + d
    def reset(self):
        seed = random.randint(0, 12423957892365781364)
        random.seed(seed)
        s = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        d = ''.join(random.choice(string.digits) for _ in range(3))
        self.name = s + d