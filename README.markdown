Text Editor Actions for Coda
----------------------------

Text Editor Actions (TEA) for Coda (formerly Textmate Emulation Applescripts)
are some of the text manipulations that I think ever editor should have,
implemented as a [Coda][1] plugin. I originally began work on TEA because
I was interested in Coda's all-in-one workflow but completely uninterested
in abandoning Textmate's excellent HTML editing capabilities.

For more information, including documentation and downloads, please see
the TEA for Coda site:

**<http://onecrayon.com/tea/coda/>**

**Found something about TEA that makes you unhappy?** [Submit a bug report
or feature request][2] (requires free GitHub account) or [drop me a line][3].

   [1]: http://panic.com/coda/
   [2]: http://github.com/onecrayon/tea-for-coda/issues
   [3]: http://onecrayon.com/about/contact/

Building from source
====================

If you want to try the latest development version of Coda, you can download
and build the plugin from source (easy_install py2app if you don't already
have it) like so:

	git clone git://github.com/onecrayon/tea-for-coda.git
	cd tea-for-coda
	python setup.py py2app

If you wish to create a development version, you can run this instead:

	python setup.py py2app -A

This will create a normal version of the TEA plugin, but symlink all the
internal files so that you don't have to rebuild the plugin to try out
changes (you'll still need to relaunch Coda between changes, though).