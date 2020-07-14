easy-text-summarization
==================


Let's do it gradually together, step by step.

Installation
------------

::

    python setup.py develop


Tutorial
--------

1. simple start
~~~~~~~~~~~~~~~

run:

``easy-text-summarization train cfg/tf.json``

and you will see the training start with the input documents specified in
the config file.


Usage
-----

TRAIN: (example config\_file can be found in cfg/)

``easy-text-summarization train config_file``

PROCESS BATCH:

``easy-text-summarization predict config_file [output_folder] [test_set_name]``
