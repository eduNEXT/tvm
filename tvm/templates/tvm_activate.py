"""Tutor switcher jinja template."""
from jinja2 import Template

TEMPLATE = '''
# This file must be used with "source bin/activate" *from bash*
# you cannot run it directly
if [ "${BASH_SOURCE-}" = "$0" ]; then
    echo "You must source this script: \$ source $0" >&2
    exit 33
fi
tvmoff () {
    # reset old environment variables
    # ! [ -z ${VAR+_} ] returns true if VAR is declared at all
    if ! [ -z "${_TVM_OLD_VIRTUAL_PATH:+_}" ] ; then
        PATH="$_TVM_OLD_VIRTUAL_PATH"
        export PATH
        unset _TVM_OLD_VIRTUAL_PATH
    fi
    if ! [ -z "${_TVM_OLD_TUTOR_ROOT:+_}" ] ; then
        TUTOR_ROOT="$_TVM_OLD_TUTOR_ROOT"
        export TUTOR_ROOT
        unset _TVM_OLD_TUTOR_ROOT
    else
        unset TUTOR_ROOT
    fi
    if ! [ -z "${_TVM_OLD_TUTOR_PLUGINS_ROOT:+_}" ] ; then
        TUTOR_PLUGINS_ROOT="$_TVM_OLD_TUTOR_PLUGINS_ROOT"
        export TUTOR_PLUGINS_ROOT
        unset _TVM_OLD_TUTOR_PLUGINS_ROOT
    else
        unset TUTOR_PLUGINS_ROOT
    fi
    # The hash command must be called to get it to forget past
    # commands. Without forgetting past commands the $PATH changes
    # we made may not be respected
    hash -r 2>/dev/null
    if ! [ -z "${_TVM_OLD_VIRTUAL_PS1+_}" ] ; then
        PS1="$_TVM_OLD_VIRTUAL_PS1"
        export PS1
        unset _TVM_OLD_VIRTUAL_PS1
    fi
    unset VIRTUAL_ENV
    if [ ! "${1-}" = "nondestructive" ] ; then
    # Self destruct!
        unset -f tvmoff
    fi
}
# unset irrelevant variables
tvmoff nondestructive
TVM_PROJECT_ENV="$PWD/.tvm"
export TVM_PROJECT_ENV
_TVM_OLD_VIRTUAL_PATH="$PATH"
PATH="$TVM_PROJECT_ENV/bin:$PATH"
export PATH
if ! [ -z "${TUTOR_ROOT+_}" ] ; then
    _TVM_OLD_TUTOR_ROOT="$TUTOR_ROOT"
fi
TUTOR_ROOT="{{ tutor_root }}"
export TUTOR_ROOT
if ! [ -z "${TUTOR_PLUGINS_ROOT+_}" ] ; then
    _TVM_OLD_TUTOR_PLUGINS_ROOT="$TUTOR_PLUGINS_ROOT"
fi
TUTOR_PLUGINS_ROOT="{{ tutor_plugins_root }}"
export TUTOR_PLUGINS_ROOT
_TVM_OLD_VIRTUAL_PS1="${PS1-}"
if [ "x{{version}}" != x ] ; then
    PS1="[{{version}}] ${PS1-}"
else
    PS1="(`basename \"$VIRTUAL_ENV\"`) ${PS1-}"
fi
export PS1
# The hash command must be called to get it to forget past
# commands. Without forgetting past commands the $PATH changes
# we made may not be respected
hash -r 2>/dev/null
'''

TVM_ACTIVATE_SCRIPT = Template(TEMPLATE)
