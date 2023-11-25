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
     name='goodnews',
     version='0.0.1',
     description="Open-source platform for curating personalized, positive news",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/GAI-Curator/news-curator",
     packages=setuptools.find_packages(),
     install_requires=reqs,
     include_package_data=True,
     package_data={'': ['*.ini']},  # If any package contains *.ini files, include them
     scripts=[],
     entry_points={'console_scripts': []},
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
         "Topic :: Scientific/Engineering :: Artificial Intelligence",
     ],
 )
