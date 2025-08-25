import setuptools
from pathlib import Path

root = Path(__file__).parent

setuptools.setup(
    name="nstools",
    version="1.2.3",
    url="https://github.com/seiya-dev/NSTools",
    long_description=(root / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    license="MIT",
    license_files=["LICENSE.md"],

    package_dir={"": "py"},               # relative to setup.py
    packages=setuptools.find_packages(where="py"),

    scripts=[
        "build/bin/ns-verify-folder",
        "build/bin/ns-verify-folder-log",
        "build/bin/ns-verify-folder.bat",
        "build/bin/ns-verify-folder-log.bat",
        "build/ns_verify_folder.py",
    ],

    install_requires=[
        "zstandard",
        "enlighten",
        "requests",
        "pycryptodome",
    ],

    python_requires=">=3.10",
    zip_safe=True,
    include_package_data=True,
)
