from os.path import join
from pathlib import Path

from uber.config import c, parse_config
from uber.jinja import template_overrides
from uber.utils import mount_site_sections, static_overrides

from magwest._version import __version__  # noqa: F401
from magwest.config import *


mount_site_sections(config['module_root'])
static_overrides(join(config['module_root'], 'static'))
template_overrides(join(config['module_root'], 'templates'))


# These need to come last so they can make use of config properties
from magwest.automated_emails import *  # noqa: F401,E402,F403
from magwest.models import *  # noqa: F401,E402,F403
