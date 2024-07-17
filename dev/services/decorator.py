class cached_property(object):
    """
    Descriptor that mimics the behavior of @property but caches the result.

    This decorator is used to cache the result of a property method, so that the method
    is only called once per instance. Subsequent accesses to the property will return
    the cached value, rather than recomputing it.

    Example:
        class MyClass(object):
            @cached_property
            def my_property(self):
                print("Computing the value")
                return 42

        obj = MyClass()
        print(obj.my_property)  # First access, prints "Computing the value" then "42"
        print(obj.my_property)  # Subsequent access, prints "42" without recomputing

    Methods:
        __init__(func): Initializes the cached_property with the function to be cached.
        __get__(instance, owner): Retrieves the cached value if it exists, otherwise
                                  computes and caches the value.
    """

    def __init__(self, func):
        self.func = func
        # Preserve property name and doc string
        self.__name__ = func.__name__
        self.__doc__ = getattr(func, "__doc__")

    def __get__(self, instance, owner):
        # If accessing the property on the class, return the cached_property object itself.
        if instance is None:
            return self

        # Check if the value is already cached.
        value = instance.__dict__.get(self.__name__)

        # If not cached, compute the value.
        if value is None:
            value = self.func(instance)
            instance.__dict__[self.__name__] = value

        return value  # Return the cached value.
