import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='kmy-venom',
    version='0.1.0',
    packages = find_packages(),
    include_package_data=True,
    description='bind blackdoor into apk/exe file.',
    long_description = README,
    long_description_content_type='text/markdown',
    author='Exso Kamabay',
    url='https://github.com/ExsoKamabay/',
    license='Apache License 2.0',
    install_requires=['kmy-beautify==0.6.0','bs4','requests'],
    keywords = ['kamabay', 'venom'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    entry_points={
        "console_scripts":[
            "venom = venom.venom:main"
        ]
    }
)