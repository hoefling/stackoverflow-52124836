from .covplugin import IstanbulPlugin

def coverage_init(reg, options):
    reg.add_file_tracer(IstanbulPlugin())
