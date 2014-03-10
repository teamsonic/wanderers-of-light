import os, web
from jinja2 import Environment, FileSystemLoader


def render(name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(
        loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')),
        extensions=extensions,
    )
    jinja_env.globals.update(globals)

    return jinja_env.get_template(name).render(context)
