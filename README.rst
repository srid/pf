pf
==

Since I got frustrated typing ``less src/foo/bar/baz/afile.py`` all the time, 
I wrote this tool. How to use it? You can find it yourself by just playing 
with it.

No PyPI release yet; so to install it right now::

    sudo pip install -e git://github.com/srid/pf.git#egg=pf

Some notes
----------

- If there are multiple matches ... after entering the index of the match, only
  the choosen match will be printed to stdout. So you can pass that one to your
  text editor or something: ``vim `bin/pf xml patch```

Credits
-------

- `Distribute`_
- `Buildout`_
- `modern-package-template`_

.. _Buildout: http://www.buildout.org/
.. _Distribute: http://pypi.python.org/pypi/distribute
.. _`modern-package-template`: http://pypi.python.org/pypi/modern-package-template
