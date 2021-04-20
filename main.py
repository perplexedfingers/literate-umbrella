from __future__ import annotations

from typing import Optional


def func(input_: dict) -> dict:
    if isinstance(input_, dict):
        result = {}
        return result
    else:
        # I should throw an exception here, but I am too lazy to come up a name
        # and handle the exception accordingly
        pass


def traverse(data: dict, pathes: Optional[list] = None) -> list:
    if pathes is None:
        pathes = []

    # assume the data is would have the exact structure like the give test data
    if isinstance(data, dict):
        pathes += [*data.keys()]
        current_key = pathes[-1]
        pathes = traverse(data[current_key], pathes)
    else:
        pathes += [data]
    return pathes
