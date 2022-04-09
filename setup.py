from setuptools import setup, find_packages

setup(
    name='tbnu',
    version='0.1.3',
    license='MIT',
    description='TBNU is a super simple and easy to use CLI notes application',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keyword="notes, cli, note application",
    url='https://github.com/PhantomLel/tbnu',
    packages= find_packages(),
    entry_points={
        'console_scripts' : [
            'tbnu=tbnu:main'
        ]
    },
    python_requires='>=3.6',
    author='Abdullah Mohammed',
    author_email='aamohammed4556@gmail.com',
    install_requires=["appdirs>=1.4.4"]
)
