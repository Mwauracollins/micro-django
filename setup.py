from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='micro-django',
    version='0.1.0',
    author='Mwaura Collins',
    author_email='mwauracollinss1@gmail.com',
    description='A simplified version of Django for educational purposes',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mwauracollins/micro-django",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'microdjango-admin=microdjango.core.management:execute_from_command_line',
        ],
    },
)
