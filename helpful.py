from typing import Optional, Union, Dict, List


def fullmax(iterable: Union[List, Dict], *, key_func=None, minimum=False, allow_none=False, full_result=False) -> \
        Optional[tuple]:
    """Functions like "max", except it returns both the key and the
    value as a pair.
    key_func will be applied to the values, before sorting by this key.
    it defaults to the identity function.

    Will call key_func once or twice for each key (works in two-pass).

    Use "minimum=True" if you want a minimum.
    Use "allow_none=True" to make empty iterables return None.
    Use "full_result=True" to return a triplet - third is the calculated value."""
    if key_func is None:
        def identity(x):
            return x

        key_func = identity
    if len(iterable) == 0:
        if allow_none:
            return None
        raise ValueError(f"Empty {type(iterable)} in fullmax.")
    iterable_keys = iterable.keys() if isinstance(iterable, dict) else range(len(iterable))
    iterable_values = [iterable[k] for k in iterable_keys]
    if minimum:
        best_value = min(iterable_values, key=key_func)
    else:
        best_value = max(iterable_values, key=key_func)
    for key in iterable_keys:
        value = iterable[key]
        if value == best_value:
            if full_result:
                return key, value, key_func(value)
            else:
                return key, value
    raise AssertionError("Should have returned already.")


assert fullmax([1, 2, 3]) == (2, 3)
assert fullmax([1, 2, 3], minimum=True) == (0, 1)
assert fullmax(["a", "b"]) == (1, "b")
assert fullmax({2: 3, 1: 2, 5: 1}) == (2, 3)
assert fullmax([], allow_none=True) is None
assert fullmax([(1, 2, 3), (1, 2, 9), (2, 3, 4)], key_func=lambda t: sum(t)) == (1, (1, 2, 9))
assert fullmax([(1, 2, 3), (1, 2, 9), (2, 3, 4)], key_func=lambda t: sum(t), full_result=True) == (1, (1, 2, 9), 12)


def argmax(iterable, **kwargs) -> Optional[tuple]:
    result = fullmax(iterable, **kwargs)
    if result is None:
        return None
    else:
        return result[0]


assert argmax([6, 1, 7, 4]) == 2
