import collections
import json
import os
import pathlib

import coverage.plugin


class FileReporter(coverage.plugin.FileReporter):

    def source(self):
        with open(self.filename) as fp:
            js = fp.read()
        return js

    def lines(self):
        return {i + 1 for i, line in enumerate(self.source().split(os.linesep)) if line.strip()}


class IstanbulPlugin(coverage.plugin.CoveragePlugin, coverage.plugin.FileTracer):

    def file_reporter(self, filename):
        return FileReporter(filename)

    def file_tracer(self, filename):
        return None

    def find_executable_files(self, src_dir):
        yield from (str(p) for p in pathlib.Path(src_dir).rglob('*.js')
                    if not any(d in p.parts for d in ('node_modules', 'coverage',)))
