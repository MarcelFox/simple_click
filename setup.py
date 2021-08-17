from setuptools import setup, find_packages

setup(
    name='app',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'simple_click = app.main:cli',
        ],
    },
)