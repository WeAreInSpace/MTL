from setuptools import setup

setup(
    name='mtlhtml',
    version='1.1',
    description='A tool that help you to write HTML in Python',
    long_description='''### Write HTML in Python with MTL''',
    long_description_content_type='text/markdown',
    url='https://github.com/WeAreInSpace/MTL',
    author='WeAreInSpace',
    author_email='weareinspace.net@gmail.com',
    license='MIT',
    keywords='html in python website ssg',
    packages=['mtl'],
    package_dir={'mtl': 'src/mtl'},
    package_data={'mtl': ['css/*.py']}
)