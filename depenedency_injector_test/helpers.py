class Helper(object):
    def __init__(self, num: int):
        self.num = num

    def action(self, a):
        pass


class Helper01(Helper):
    def action(self, a):
        return a * self.num


class Helper02(Helper):
    def action(self, a):
        return a / self.num


class Helper03(Helper):
    def action(self, a):
        return a + self.num


helpers_dict = {'Helper01': Helper01, 'Helper02': Helper02, 'Helper03': Helper03}
