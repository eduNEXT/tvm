"""Tutor switcher jinja template."""
from jinja2 import Template

TEMPLATE = '''
{% if tutor_root %}
echo -e "Using the \033[1;32m{{ config_name }}\033[0m config" >&2
export TUTOR_ROOT={{ tutor_root }}
export TUTOR_PLUGINS_ROOT={{ tutor_root }}/inline_plugins
{% else %}
echo -e "You have not selected any config. Tutor will use the global default \033[1;31m~.local/share/tutor\033[0m"
{% endif %}
{% if version %}
{{ tvm }}/{{ version }}/venv/bin/tutor $@
{% else %}
echo "You need to select a tutor active version at first. Run 'stack tvm use <VERSION>'"
{% endif %}
'''

TUTOR_SWITCHER_TEMPLATE = Template(TEMPLATE)
