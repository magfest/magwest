from os.path import join

from sideboard.lib import parse_config
from uber.jinja import template_overrides
from uber.utils import mount_site_sections, static_overrides

from magwest._version import __version__  # noqa: F401


config = parse_config(__file__)
mount_site_sections(config['module_root'])
static_overrides(join(config['module_root'], 'static'))
template_overrides(join(config['module_root'], 'templates'))


# These need to come last so they can make use of config properties
from magwest.automated_emails import *  # noqa: F401,E402,F403
