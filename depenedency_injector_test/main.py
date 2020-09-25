from dependency_injector import containers, providers

from depenedency_injector_test.helpers import helpers_dict


class Container(containers.DeclarativeContainer):
    helper = providers.Callable(helpers_dict['Helper03'])


container = Container()

print(container.helper(num=5).action(20))
