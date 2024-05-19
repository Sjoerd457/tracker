from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        # List your project's dependencies here.
        # Example: 'requests>=2.23.0',
    ],
    entry_points={
        "console_scripts": [
            # Define command-line scripts here.
            # Example: 'my_command = my_package.module:function',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)