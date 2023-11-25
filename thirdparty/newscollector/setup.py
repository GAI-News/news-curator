import setuptools


def read_requirements_file(path):
    reqs = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            reqs.append(line.split('==')[0])
    return reqs


with open("README.md", "r") as fh:
    long_description = fh.read()

reqs = read_requirements_file('requirements.txt')

setuptools.setup(
     name='newscollector',
     version='0.1.0',
     description="Open-source platform for downloading and curating news from select news sources",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/elisemercury/NewsCollector",
     packages=setuptools.find_packages(),
     install_requires=reqs,
     include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
         "Topic :: Scientific/Engineering :: Artificial Intelligence",
     ],
 )
