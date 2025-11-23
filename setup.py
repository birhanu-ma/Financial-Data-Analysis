from setuptools import setup, find_packages

setup(
    name='nova_financial_insights', # Choose a name for your package
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)