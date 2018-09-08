import collections
import io
import json

import coverage.data
import pytest


def nested_iter(nested):
    for key, value in nested.items():
        if isinstance(value, collections.Mapping):
            for inner_key, inner_value in nested_iter(value):
                yield inner_key, inner_value
        else:
            yield key, value


def line_numbers(item):
    return sorted(set((value for key, value in nested_iter(item) if key == 'line')))


@pytest.fixture(autouse=True)
def append_istanbul_coverage(cov):
    yield

    with open('coverage/coverage.json') as fp:
        data = json.load(fp)
    converted = {'lines': {item['path']: line_numbers(item) for item in data.values()}}
    text = "!coverage.py: This is a private format, don't read it directly!" + json.dumps(converted)
    istanbul_cov = coverage.data.CoverageData()

    with io.StringIO(text) as fp:
        istanbul_cov.read_fileobj(fp)
    cov.data.update(istanbul_cov)
