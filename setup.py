from setuptools import setup

setup(
    name='tkdown',
    version='1.0',
    install_requires=[
        'tkinter',
        're',
        'importlib-metadata; python_version >= "2.0"',
        'pillow',
    ],
    url="https://github.com/TheRealPenguin12/tkdown",
    author="_TheRealPenguin",
    keywords="python python3 python-3 module tkinter app markdown easy awesome",
    license="MIT",
    description="Markdown for Tkinter.",
    classifiers=[
	    "Development Status :: 2 - Pre-Alpha",
	    "License :: OSI Approved :: MIT License",
	    "Natural Language :: English",
	    "Programming Language :: Python :: 3",
	    "Topic :: Utilities",
	    "Intended Audience :: Developers",
    ]
)
