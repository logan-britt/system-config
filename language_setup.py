import os
import sys
import shutil
import platform
import subprocess

'''
    Here we have the setup functions for the system programming languages.
    They download the compilers and the package managers for the
    language ecosystem.
'''
def c_lang(build_system, clean_up=False):
    if platform.system() == 'Linux':
        if 'arch' in platform.platform():
            if build_system == 'meson':
                subprocess.run(
                    ['pacman', '-S', 'meson', 'ninja', 'gcc', 'clang'])

            elif build_system == 'cmake':
                subprocess.run(
                    ['pacman', '-S', 'cmake', 'gcc', 'clang'])

            else:
                raise ValueError('This build system is not supported.')

        elif 'ubuntu' in platform.platform():
            pass

        else:
            raise RuntimeError('This distro is not supported.')

    elif platform.system() == 'Darwin':
        pass

    elif platform.system() == 'Windows':
        pass

    else:
        RuntimeError('This operating system is not supported.')

def rust_lang(clean_up=False):
    if platform.system() == 'Linux':
        if 'arch' in platform.platform():
            pass

        elif 'ubuntu' in platform.platform():
            pass

        else:
            raise RuntimeError('This distro is not supported.')

    elif platform.system() == 'Darwin':
        pass

    elif platform.system() == 'Windows':
        pass

    else:
        raise RuntimeError('')

'''
    These languages are the scripting languages that can be used for system
    managment and quick processes.
'''

def javascript_lang(clean_up=False):
    pass

def groovy_lang(clean_up=False):
    pass

'''
    These languages are functional languages, witch at the moment is just
    haskell.
'''

def haskell_lang(clean_up=False):
    pass

if __name__ == '__main__':
    # here we process the command line arguments
    unprocessed_args = sys.argv[1:]
    processed_args = {}

    for arg in unprocessed_args:
        split_data = arg.split(' ')
        split_data[0] = split_data[0].lstrip('-')

        if split_data[0] == 'c':
            processed_args['c'] = 'add'

        elif split_data[0] == 'rust':
            processed_args['rust'] = 'add'

        elif split_data[0] == 'js':
            processed_args['js'] = 'add'
        
        elif split_data[0] == 'groovy':
            processed_args['groovy'] = 'add'

        elif split_data[0] == 'haskell':
            processed_args['haskell'] = 'add'

        else:
            raise ValueError(f'This argument is not supported: {split_data}')
    
    # here we run the install language tool chains
    for arg in processed_args:
        if arg == 'c':
            c_lang()

        elif arg ==  'rust':
            rust_lang()
