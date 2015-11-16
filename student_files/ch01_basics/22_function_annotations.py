def display_info(name: str, age: int, spouse: str, *children: tuple, parents: list, **other_family: dict) -> dict:
    return display_info.__annotations__


print(display_info('John', 40, 'Sally', 'Tim', 'Sam', parents=['Martha', 'Frank'], sister='Amy'))


# another example:
def foo(x: 'a number value to square') -> 'the square of the input':
    return x*x
