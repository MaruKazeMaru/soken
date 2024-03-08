from setuptools import setup, find_packages

def get_requires():
    with open('requirements.txt') as f:
        requires = f.readlines()
    return requires


setup(
    name='konryu',
    version='0.0.0',
    description='minimum Jinja2 CLI tool',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    author='ShinagawaKazemaru',
    author_email='marukazemaru0@gmail.com',
    license='MIT',

    include_package_data=True,
    install_requires=get_requires(),
    python_requires='>=3.9',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    entry_points={
        'console_scripts': [
            'konryu=konryu._cli:make',
        ]
    },
)
