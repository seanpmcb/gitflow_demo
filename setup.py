from setuptools import setup, find_packages

import gitflow_demo

setup(name='gitflow_demo',
      version=gitflow_demo.__version__,
      description='Gitflow Demo',
      packages=find_packages(),
      classifiers=[
          'Development Status :: 1 - Alpha',
          'Programming Language :: Python',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules', ],
      zip_safe=False,
      )
