from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> None:
        if args not in storage:
            print("Calculating new result")
            storage[args] = func(*args)
        else:
            print("Getting from cache")
        return storage[args]
    return wrapper
