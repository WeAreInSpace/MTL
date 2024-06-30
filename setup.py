from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='MTL',
    version='1.0',
    description='A tool that help you to write HTML in Python',
    long_description=readme(),
    url='https://github.com/WeAreInSpace/MTL',
    author='We Are In Space',
    author_email='weareinspace.net@gmail.com',
    license='MIT',
    install_requires=[
        'matplotlib',
        'numpy',
    ],
    keywords='html in python website ssg',
    packages=['mtl'],
    package_dir={'mtl': 'src/mtl'},
    package_data={'mtl': ['css/*.py']
    },
)