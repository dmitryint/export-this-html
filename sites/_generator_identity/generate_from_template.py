# -*- coding: utf-8 -*-

"""GenerateFromTemplate.
Install requirements: pip3 install jinja2
Usage:
  generate_from_template.py     (--template=<TEMPLATE_FILE>)
                                (--env=<ENV_FILE>)
"""

from docopt import docopt
from jinja2 import Environment, FileSystemLoader
import os

arguments = docopt(__doc__, version='GenerateFromTemplate')

TEMPLATE_FILE = arguments['--template']
ENV_FILE = arguments['--env']


def read_env(env_file):
    d = {}
    with open(env_file) as f:
        for line in f:
            (key, val) = line.strip().split('=', maxsplit=1)
            d[str(key)] = str(val.strip('\' '))
    return d


j2_env = Environment(
    loader=FileSystemLoader(
        os.path.dirname(
            os.path.abspath(TEMPLATE_FILE)
        )),
    trim_blocks=True
)

print(
    j2_env.get_template(
        os.path.basename(TEMPLATE_FILE)
    ).render(**read_env(ENV_FILE))
)
