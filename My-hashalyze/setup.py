from setuptools import setup, find_packages

setup(
    name='hashalyze',
    version='1.0.0',
    author='Advik',
    description='A CLI tool to identify hash types like a boss 🧠',
    packages=find_packages(),
    py_modules=['main', 'cli'],
    install_requires=[
        'pyfiglet',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'hash-id=cli:run_cli',
        ],
    },
)
entry_points={
    'console_scripts': [
        'hash-id=cli:run_cli',
    ],
}
