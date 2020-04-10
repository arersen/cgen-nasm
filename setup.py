from setuptools import setup

NAME = "cgen_nasm"
DESCRIPTION = "NASM Code generator"
URL = "https://github.com/qbaddev/cgen-nasm"
EMAIL = "yavarenikya@gmail.com"
AUTHOR = "qbaddev"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "1.0.0"

REQUIRED = []

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = DESCRIPTION,
    long_description_content_type = "text/markdown",
    author = AUTHOR,
    author_email = EMAIL,
    python_requires = REQUIRES_PYTHON,
    url = URL,
    packages = ["cgen_nasm"],
    entry_points = {
        "console_scripts": ["b0mb3r=b0mb3r.__main__:main", "bomber=b0mb3r.__main__:main",]
    },
    install_requires = REQUIRED,
    extras_require = {},
    package_data = {"cgen_nasm": ["/*/*"]},
    license = "GNU General Public License v3.0",
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Internet",
        "License :: OSI Approved :: GNU General Public License v3.0",
    ],
)
