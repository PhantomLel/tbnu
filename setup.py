from setuptools import setup

setup(
    name='tbnu',
    version='X.YaN',
    license='MIT',
    description='TBNU is a super simple and easy to use CLI notes application',
    long_description=open('README.md').read(),
    url='https://github.com/PhantomLel/tbnu',
    entry_points='''
        [console_scripts]
        tbnu=tbnu.__main__:main
    ''',
    include_package_data=True,
    package_data={'tbnu': ['db.pkl']},
    author='Abdullah Mohammed',
    author_email='aamohammed4556@gmail.com'
)