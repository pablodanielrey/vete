from setuptools import setup, find_packages, find_namespace_packages

setup(name="vete_models",
    version="0.0.1",
    package_dir={"":"src"},
    packages=find_namespace_packages(where="src"),
    install_requires=[
        'vete_entities',
        'inject',
        'SQLAlchemy'
    ]
)