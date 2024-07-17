from functools import partial


def lift(func):
    """
    Lift a function on values into a function on iterables

    args:
        Callable[A, B]): A function that takes an argument of type A and returns
            a value of type B

    returns:
        Callable[Iterable[A], list[B]]: A new function that takes iterables of
            type A and returns a list of type B

    Example:
        def square(x):
            return x * x

        lifted_square = lift(square)
        result = lifted_square([1, 2, 3, 4])
        print(result) # Output: [1, 4, 9, 16]
    """
    return partial(map, func)
