#!/usr/bin/env python3

tpl = '''
script:
    - some_stuff.bash

matrix:
  include:
{%- for letter, number in vars %}
    - env: TESTS={{number}} CONFIG={{letter}}
{%- endfor %}

'''

import os
import jinja2
from itertools import product

tpl = jinja2.Template(tpl)
ymlfn = os.path.join(os.path.dirname(__file__), '.travis.yml')
with open(ymlfn, 'wt') as yml:
    yml.write(tpl.render(vars=product(['a', 'b'], range(5))))
