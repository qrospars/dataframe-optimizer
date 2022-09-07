from setuptools import setup

setup(
    name='dataframe_optimizer',
    version='0.1.0',
    description='A Python package that give utils to optimize Pandas dataframes',
    url='https://github.com/qrospars/dataframe-optimizer',
    author='Quentin Rospars',
    author_email='rospars.quentin@outlook.com',
    license='BSD 2-clause',
    packages=['dataframe_optimizer'],
    install_requires=['pandas',
                      'numpy',
                      ],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
