dockerignore-generate
=====================

Python 3 cli tool to automatically generate ``.dockerignore`` files

Install
-------

.. code:: bash

   pip install dockerignore-generate

Usage
-----

In a directory with a ``Dockerfile``

.. code:: bash

   dockerignore-generate 

will print out the contents of the generated ``.dockerignore`` file.
Without arguments the docker build context is assumed to be the curret
working directory.

Contexts and Dockerfiles
~~~~~~~~~~~~~~~~~~~~~~~~

To speciify a specific context use the ``-c`` flag, and ``-f`` to
speciify a ``Dockerfile``, e.g.,

.. code:: bash

   dockerignore-generate -f Dockerfile.custom  -c ../

To save a the ``.dockerignore`` file, use the ``-s`` flag, and ``-o`` to
overwrite an existing file (file will be stored in the docker build
context)

.. code:: bash

   dockerignore-generate -f Dockerfile.custom  -c ../ -s
   wrote ../.dockerignore
