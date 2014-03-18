import os, web, threading
from jinja2 import Environment, FileSystemLoader

import config

template_root = os.path.join(os.path.abspath('.'), 'templates')



class RelativePathEnv(Environment):
    """
    Templates 'extends' block relative to template path by default
    """
    

    def join_path(self, template, parent):	
        if template.startswith('/'):
            return template[1:]
        else:
            parent_dirname = os.path.dirname(parent)
            return os.path.join(parent_dirname, template)



JENVS = threading.local()

def getThreadsJENV():
    """
    Get a Jinja Environment for this thread.
    """
    global JENVS
    jenv = getattr(JENVS, 'JENV', None)
    if not jenv:
        loader = FileSystemLoader(template_root, encoding='utf-8')
        jenv = RelativePathEnv(
            block_start_string='[[',
            block_end_string=']]',
            variable_start_string='[-',
            variable_end_string='-]',
            comment_start_string='[#',
            comment_end_string='#]',
            loader=loader,
            extensions=[],
            cache_size=50,
        )
        JENVS.JENV = jenv
    return jenv


def _render(template_name, params=None):
    if params is None:
        params = {}
    template = getThreadsJENV().get_template(template_name)
    return template.render(params)


def render(template_name, params=None):
    request_params = web.ctx.get('_jinja_variables', {})
    request_params.update(params or {})
    return _render(template_name, request_params)

