import os
import sys
import shutil
import platform

'''
  These functions pretain to text and text based programs (tui's). These
  functions will download the programs and run the nessisary config scrips
  so that the enviroment has a standerdised structure across all possible
  systems.
'''

def neovim(clean_up=False):
  if platform.system() == 'Linux':
    if 'arch' in platform.platform():
      os.system('pacman -S neovim')
      print()

    elif 'ubuntu' in platform.platform():
      os.system('apt install neovim')
      print()

    else:
      raise RuntimeError('This distro is not supported.')

  elif platform.system() == 'Darwin':
    pass

  elif platform.system() == 'Windows':
    pass

  else:
    raise RuntimeError('This system does not support neovim.')

  os.system('git clone https://github.com/logan-britt/neovim-config.git')
  print()

  os.chdir('neovim-config')
  os.system('python install.py')
  os.chdir('..')

  if clean_up:
    shutil.rmtree('neovim-config')

def tmux(clean_up=False):
  if platform.system() == 'Linux':
    if 'arch' in platform.platform():
      os.system('pacman -S tmux')
      print()

    elif 'ubuntu' in platform.platform():
      os.system('apt install tmux')
      print()

    else:
      raise RuntimeError('This distro is not supported.')

  elif platform.system() == 'Darwin':
    pass

  else:
    raise RuntimeError('This system does not support tmux.')

  os.system('git clone https://github.com/logan-britt/tmux-config.git')
  print()

  os.chdir('tmux-config')
  os.system('python install.py')
  os.chdir('..')

  if clean_up:
    shutil.rmtree('tmux-config')

def powerline(clean_up=False):
  if platform.system() == 'Linux':
    if 'arch' in platform.platform():
      pass

    elif 'ubuntu' in platform.platform():
      pass

    else:
      raise RuntimeError('This distro is not supported.')

  elif platform.system() == 'Darwin':
    pass

  else:
    raise RuntimeError('This system does not support powerline statusbar.')

def zsh(clean_up=False):
  if platform.system() == 'Linux':
    if 'arch' in platform.platform():
      os.system('pacman -S zsh')
      print()

    elif 'ubuntu' in platform.platform():
      os.system('apt install zsh')
      print()

    else:
      raise RuntimeError('This distro is not supported.')

  elif platform.system() == 'Darwin':
    pass

  else:
    raise RuntimeError('This system does not support zsh.')

  os.system('git clone https://github.com/logan-britt/zsh-config.git')
  print()

  os.chdir('zsh-config')
  os.system('python install.py')
  os.chdir('..')

  if clean_up:
    shutil.rmtree('zsh-config')

def w3m(clean_up=False):
  if platform.system() == 'Linux':
    if 'arch' in platform.platform():
      os.system('pacman -S w3m')
      print()

    elif 'ubuntu' in platform.platform():
      os.system('apt install w3m')
      print()

    else:
      raise RuntimeError('This distro is not supported.')

  elif platform.system() == 'Darwin':
    pass

  else:
    raise RuntimeError('This system does not support w3m.')

  os.system('git clone https://github.com/logan-britt/w3m-config.git')
  print()

  os.chdir('w3m-config')
  os.system('python install.py')
  os.chdir('..')

  if clean_up:
    shutil.rmtree('w3m-config')

'''
  These functions pretain to graphics and graphics based programs (gui's).
  These functions will download the programs and run the nessisary config
  scrips so that the enviroment has a standerdised structure across all
  possible systems.
'''

def i3(clean_up=False):
  pass

def dwm(clean_up=False):
  pass

'''
  These functions pretain to the running of different internet types (tor),
  and different vpn setups to secure online communications. It runs line 
  every other set of config functions with a 
'''

def tor(clean_up=False):
  pass

def proton_vpn(clean_up=False):
  pass

'''

'''

def setup(clean_up=False):
  pass

def config(clean_up=False):
  pass

if __name__ == '__main__':
  arguments = sys.argv

  package = {}
  if arguments[1].lstrip('-') == 'run':
    package['mode'] = 'run'

    # process the arguments for the setup command
    for i in range(2, len(arguments)):
      pass

  elif arguments[1].lstrip('-') == 'config':
    package['mode'] = 'config'

    # process the arguments for the config command
    for i in range(2, len(arguments)):
      pass

  else:
    raise ValueError('The first argument must be either --run or --config.')

  # now that we have the processed arguments, we run the approprieate function
