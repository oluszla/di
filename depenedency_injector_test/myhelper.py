import helpers

class MyHelper(helpers.Helper):
    def action(self, a):
        print("MyHelper")
        return a - self.num

helpers.helpers_dict["MyHelper"] = MyHelper
