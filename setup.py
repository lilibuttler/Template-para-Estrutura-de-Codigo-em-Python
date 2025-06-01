from setuptools import setup, find_packages

setup(
    name='meu_projeto',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0',
    ],
    entry_points={{
        'console_scripts': [
            'meu_projeto=meu_projeto.scripts.run:main',
        ],
    }},
)
