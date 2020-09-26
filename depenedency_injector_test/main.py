from dependency_injector import containers, providers
from helpers import helpers_dict
import importlib
import sys



def importHelper(helper_name):
    return importlib.import_module(helper_name)

importHelper(sys.argv[1])

class Container(containers.DeclarativeContainer):
    helper = providers.Callable(helpers_dict['MyHelper'])


container = Container()

print(container.helper(num=5).action(20))
