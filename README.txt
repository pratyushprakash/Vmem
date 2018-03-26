The package requires pin v3.6 to be installed

The Environment variable PIN_ROOT must be set to the directory of
pin executable.


The program is compiled by
$>make obj-intel64/MemTrace.so

and run by
$>`Path to pin executable` -t `Path to MemTrace.so` -- ls

to produce output file MemTrace.so

This data can be proceesed for the classifiers with the python script.

(Python Shell)>>>data = get_data('MemTrace.out')

The data can then be fed to the classifiers.
