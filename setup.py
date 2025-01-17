import pathlib
import re
import sys
from codecs import open
from setuptools import setup, find_packages

root = pathlib.Path(__file__).parent.absolute()

with open('envclasses/__init__.py', 'r', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

with open('README.md', 'r', encoding='utf8') as f:
    readme = f.read()

setup_requires = [
    'pytest-runner',
]

requires = [
    'pyyaml',
    'typing_inspect>=0.4.0',
]

# Installs dataclasses from PyPI for python < 3.7
if sys.version_info < (3, 7):
    requires.append('dataclasses')

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-flake8',
    'mypy',
    'yapf',
    'isort',
]

docs_require = [
    'pdoc',
]

setup(
    name='envclasses',
    version=version,
    description='A library to map dataclass and environmental variables',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='yukinarit',
    author_email='yukinarit84@gmail.com',
    url='https://github.com/yukinarit/envclasses',
    packages=find_packages(exclude=['test_envclasses']),
    python_requires=">=3.6",
    setup_requires=setup_requires,
    install_requires=requires,
    tests_require=tests_require,
    extras_require={
        'docs': docs_require,
        'test': tests_require,
    },
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
