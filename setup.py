from setuptools import setup, find_packages

setup(
    name='plaspipe',
    version='0.1',
    packages=['plaspipe'],
    package_dir={'plaspipe': 'src'},
    install_requires=[
        'networkx>=2.7',
        'pandas>=2.0.0',
        'matplotlib>=3.7.0',
        'seaborn>=0.12.2',
        'biopython>=1.81',
        'scipy>=1.10.1',
        'numpy>=1.24.2',
        'scikit-learn>=0.23.1',
        'tensorflow>=2.8.0',
        'spektral>=1.0.8',
        'gurobipy>=9.1.2'
    ],
    package_data={
        'plaspipe': ['test/*.yaml']
    },
    entry_points={
        'console_scripts': [
            'plaspipe=plaspipe.plaspipe:main',
        ],
    },
    author='Ghofrane Farhat',
    author_email='ghofrane_farhat@sfu.ca',
    description='Bioinformatic pipeline for plasmid analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/GhofraneFarhat/Bioinformatic_pipeline',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)