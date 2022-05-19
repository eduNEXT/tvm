"""Tutor switcher jinja template."""
from jinja2 import Template

TEMPLATE = '''
{% if tutor_root %}
export TUTOR_ROOT={{ tutor_root }}
export TUTOR_PLUGINS_ROOT={{ tutor_plugins_root }}
{% endif %}
{% if version %}
{{ tvm }}/{{ version }}/venv/bin/tutor $@
{% else %}
echo "You need to select a tutor active version at first. Run 'tvm use <VERSION>'"
{% endif %}
'''

TUTOR_SWITCHER_TEMPLATE = Template(TEMPLATE)
