class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if len(self.card_num) < 2:
            return False
        elif self.card_num.isdigit():
            count = 1
            sp = []
            sp1 = []
            sp2 = []
            for i in self.card_num:
                sp.append(int(i))
            sp.reverse()
            for j in sp:
                if count % 2 == 0:
                    sp1.append(j*2)
                else:
                    sp1.append(j)
                count += 1
            for k in sp1:
                if k > 9:
                    sp2.append(k - 9)
                else:
                    sp2.append(k)
            if sum(sp2) % 10 == 0:
                return True
            else:
                return False
        else:
            return False
