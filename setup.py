from distutils.core import setup

setup(name='extensible-keys',
      version='v0.2.0',
      description='Reference implementation for the Extensible Key Format file format',
      author='FortunateSon1337',
      author_email='ForunateSon1337@protonmail.com',
      url = 'https://github.com/FortunateSon1337/extensible-keys',
      packages = ['extensiblekeys'],
      install_requires = ['pycryptodome'],
      license='GPLv3')
