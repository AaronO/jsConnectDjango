from setuptools import setup, find_packages

setup(
    name = "Django JsConnect",
    version = "0.1",
    packages = ['jsConnectDjango'],
    include_package_data = True,

    author = "Aaron O'Mullane",
    author_email = "aaron.omullan@gmail.com",
    description = "Authentification bridge between a Django website and VanillaForums",
    license = "Apache",
    keywords = "python django authentication vanilla forums jsconnect",
    url = "https://github.com/AaronO/jsConnectDjango",
    install_requires = [],

    classifiers = [
        'Development Status :: 0.2 - Beta Testing',
        'Environment :: Unix-like Systems',
        'Intended Audience :: Developers, Project managers, Sys admins',
        'Programming Language :: Python',
        'Operating System :: Unix-like',
    ],
)
