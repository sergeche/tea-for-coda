'''
This module includes common utility functions for working with
TEA actions, such as locating and loading them
'''

import imp
import sys
import os.path

def default_locations():
    user_modules = os.path.expanduser(
        '~/Library/Application Support/Coda/TEA/'
    )
    default_modules = os.path.expanduser(
        '~/Library/Application Support/Coda/Plug-ins/'
        'TEA for Coda.codaplugin/TEA/'
    )
    return user_modules, default_modules

def load_action(target):
    '''
    Imports target TEA action file and returns it as a module
    (TEA modules are likely not, by default, in the system path)
    
    Searches user override directory first, and then the default
    TEA scripts directory in the Sugar bundle
    
    Usage: wrap_selection_in_tag = load_action('wrap_selection_in_tag')
    '''
    user_modules, default_modules = default_locations()
    try:
        # Is the action already loaded?
        module = sys.modules[target]
    except (KeyError, ImportError):
        # Find the action (searches user overrides first)
        file, pathname, description = imp.find_module(
            target,
            [user_modules, default_modules]
        )
        if file is None:
            # Action doesn't exist
            return None
        # File exists, load the action
        module = imp.load_module(
            target, file, pathname, description
        )
    return module
