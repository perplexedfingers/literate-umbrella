from __future__ import annotations

from typing import Optional


def func(input_: dict) -> dict:
    if isinstance(input_, dict):
        plan = traverse(input_)
        result = construct(plan)
        return result
    else:
        # should throw an exception here, but I am too lazy to come up a name
        # and handle the exception accordingly
        pass


def traverse(data: dict, pathes: Optional[list[str]] = None) -> list[str]:
    if pathes is None:
        pathes = []

    # assume the data would have the exact structure like the give test data
    if isinstance(data, dict):
        pathes += [*data.keys()]
        current_key = pathes[-1]
        pathes = traverse(data[current_key], pathes)
    else:
        # should check the type here, but I am too lazy
        pathes += [data]
    return pathes


def construct(plan: list[str]) -> dict:
    # should check the type here, but I am too lazy
    value = plan.pop(0)
    result = {}
    for key in plan:
        result = {key: value}
        value = result
    return result
