from distutils.core import setup
import py2exe, sys, os

sys.argv.append("py2exe")

setup(
    options = {'py2exe': {'bundle_files': 3, 'compressed': True, 'packages': ["pynput", "pynput.keyboard"]}},
    windows = [{'script': "GuessGameKLC0.3.3.pyw"}],
    zipfile = None,)