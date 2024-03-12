userid, level = input().split()

class Nextlevel:
    def __init__(self, userid='codetree', level=10):
            self.userid = userid
            self.level = level

nextlevel1 = Nextlevel()
nextlevel2 = Nextlevel(userid, level)

print('user', nextlevel1.userid, 'lv', nextlevel1.level)
print('user', nextlevel2.userid, 'lv', nextlevel2.level)