#!/usr/bin/env python
"""Package metadata for tvm."""
import os
import re
import sys

from setuptools import find_packages, setup


def get_version(*file_paths):
    """
    Extract the version string from the file.

    Input:
     - file_paths: relative path fragments to file with
                   version string
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)

    with open(filename, 'r', encoding='utf-8') as version_file:
        version_file = version_file.read()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.

    Returns:
        list: Requirements file relative path strings
    """
    requirements = set()
    for path in requirements_paths:
        with open(path, 'r', encoding='utf-8') as requirements_file:
            requirements.update(
                line.split('#')[0].strip() for line in requirements_file.readlines()
                if is_requirement(line.strip())
            )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement.

    Returns:
        bool: True if the line is not blank, a comment, a URL, or
              an included file
    """
    return line and not line.startswith(('-r', '#', '-e', 'git+', '-c'))


VERSION = get_version('tvm', '__init__.py')

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system(f"git tag -a {VERSION} -m 'version {VERSION}'")
    os.system("git push --tags")
    sys.exit()

with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r', encoding='utf-8') as readme_file:
    README = readme_file.read()

with open(os.path.join(os.path.dirname(__file__), 'CHANGELOG.md'), 'r', encoding='utf-8') as changelog_file:
    CHANGELOG = changelog_file.read()

setup(
    name='tutor-version-manager',
    version=VERSION,
    description="""It manages Tutor versions and enables switching between them.""",
    long_description=README + '\n\n' + CHANGELOG,
    author='eduNEXT',
    author_email='contact@edunext.co',
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=load_requirements('requirements/base.in'),
    python_requires=">=3.8",
    zip_safe=False,
    keywords='Python eduNEXT Open edX Tutor',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': [
            'tvm = tvm.cli:main',
        ],
    },
)
