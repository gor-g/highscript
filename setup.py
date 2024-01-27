from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='himage',
    version='0.0.0',
    description='A small library, of high level scripting tools',
    url='https://github.com/mySpecialUsername/highscript',
    author='Gor G.',
    packages=find_packages(),
    install_requires=[xxxxx],
    python_requires='>=3.6',
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
