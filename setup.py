from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.5'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    'applib',
]


setup(name='pf',
    version=version,
    description="Programmer's find; smart file-finding; no more repeated double-tabs.",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      'Development Status :: 1 - Planning',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Intended Audience :: System Administrators',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Topic :: Software Development',
      'Topic :: Utilities',
    ],
    keywords='',
    author='Sridhar Ratnakumar',
    author_email='sridhar.ratna@gmail.com',
    url='http://github.com/srid/pf',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['pf=pf:main']
    }
)
