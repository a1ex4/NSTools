import setuptools
from pathlib import Path

appPath = Path(__file__).resolve().parent
rootPath = appPath.parent
srcPath = rootPath / "py"

readmePath = rootPath / "README.md"

long_description = ""
if readmePath.is_file():
    with open(readmePath, "r", encoding="utf-8") as rmf:
        long_description = rmf.read()

setuptools.setup(
    name="nstools",
    version="1.2.3",
    url="https://github.com/seiya-dev/NSTools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    license_files=["../LICENSE.md"],

    package_dir={"": str(srcPath)},
    packages=setuptools.find_packages(where=str(srcPath)),

    scripts=[
        "bin/ns-verify-folder",
        "bin/ns-verify-folder-log",
        "bin/ns-verify-folder.bat",
        "bin/ns-verify-folder-log.bat",
        # "../py/ns_verify_folder.py",
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
