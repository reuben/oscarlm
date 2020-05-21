import os

from setuptools import find_packages, setup


def main():
    reqs_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    with open(reqs_file) as fin:
        reqs = [l.strip() for l in fin]

    setup(
        name='oscarlm',
        version='0.0.1',
        description='Generate DeepSpeech language models from OSCAR datasets',
        url='https://github.com/mozilla/oscarlm',
        author='Mozilla',
        license='MPL-2.0',
        # Classifiers help users find your project by categorizing it.
        #
        # For a list of valid classifiers, see https://pypi.org/classifiers/
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
            'Programming Language :: Python :: 3',
        ],
        packages=find_packages(),
        python_requires='>=3.5, <4',
        install_requires=reqs,
    )

if __name__ == '__main__':
    main()
