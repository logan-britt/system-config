import os
import sys
import shutil
import platform
import subprocess

'''
  These functions pretain to text and text based programs (tui's). These
  functions will download the programs and run the nessisary config scrips
  so that the enviroment has a standerdised structure across all possible
  systems.
'''

def neovim(clean_up=False):
  if platform.system() == 'Linux':
    if 'arch' in platform.platform():
      subprocess.run(['pacman', '-S', 'neovim'])
      print()

    elif 'ubuntu' in platform.platform():
      subprocess.run(['apt', 'install', 'neovim'])
      print()

    else:
      raise RuntimeError('This distro is not supported.')

  elif platform.system() == 'Darwin':
    pass

  elif platform.system() == 'Windows':
    pass

  else:
    raise RuntimeError('This system does not support neovim.')

  subprocess.run(
        ['git', 'clone', 'https://github.com/logan-britt/neovim-config.git'])
  print()

  os.chdir('neovim-config')
  subprocess.run(['python', 'install.py'])
  os.chdir('..')

  if clean_up:
    shutil.rmtree('neovim-config')

def remove_neovim():
  if platform.system() == 'Linux':
    if 'arch' in platform.platform():
      subprocess.run(['pacman', '-Rnc', 'neovim'])
      print()

    elif 'ubuntu' in platform.platform():
      subprocess.run(['apt', 'remove ', 'neovim'])
      print()
    
    else:
      raise RuntimeError('This distro is not supported.')
    
    pass

  elif platform.system() == 'Darwin':
    pass

  elif platform.system() == 'Windows':
    pass

  else:
    raise RuntimeError('This system is not supported.')

def tmux(clean_up=False):
  if platform.system() == 'Linux':
    if 'arch' in platform.platform():
      subprocess.run(['pacman', '-S', 'tmux'])
      print()

    elif 'ubuntu' in platform.platform():
      subprocess.run(['apt', 'install', 'tmux'])
      print()

    else:
      raise RuntimeError('This distro is not supported.')

  elif platform.system() == 'Darwin':
    pass

  else:
    raise RuntimeError('This system does not support tmux.')

  subprocess.run(
        ['git', 'clone', 'https://github.com/logan-britt/tmux-config.git'])
  print()

  os.chdir('tmux-config')
  subprocess.run(['python', 'install.py'])
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
      subprocess.run(['pacman', '-S', 'zsh'])
      print()

    elif 'ubuntu' in platform.platform():
      subprocess.run(['apt', 'install', 'zsh'])
      print()

    else:
      raise RuntimeError('This distro is not supported.')

  elif platform.system() == 'Darwin':
    pass

  else:
    raise RuntimeError('This system does not support zsh.')

  subprocess.run(
          ['git', 'clone', 'https://github.com/logan-britt/zsh-config.git'])
  print()

  os.chdir('zsh-config')
  subprocess.run(['python', 'install.py'])
  os.chdir('..')

  if clean_up:
    shutil.rmtree('zsh-config')

def w3m(clean_up=False):
  if platform.system() == 'Linux':
    if 'arch' in platform.platform():
      subprocess.run(['pacman', '-S', 'w3m'])
      print()

    elif 'ubuntu' in platform.platform():
      subprocess.run(['apt', 'install', 'w3m'])
      print()

    else:
      raise RuntimeError('This distro is not supported.')

  elif platform.system() == 'Darwin':
    pass

  else:
    raise RuntimeError('This system does not support w3m.')

  subprocess.run(
          ['git', 'clone', 'https://github.com/logan-britt/w3m-config.git'])
  print()

  os.chdir('w3m-config')
  subprocess.run(['python', 'install.py'])
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
    if platform.system() != 'Linux':
        raise RuntimeError('This system is not supported.')

    if 'arch' in platform.platform():
        subprocess.run(['pacman', '-S', 'i3-gaps', 'picom', 'feh'])
        print()

        print('Setting up the aur packages.')
        subprocess.run(
                ['git', 'clone', 'https://aur.archlinux.org/polybar.git'])
        os.chdir('polybar')
        subprocess.run(['makepkg', '-si'])
        os.chdir('..')
        shutil.rmtree('polybar')
        print()

    else:
        raise RuntimeError('This distro is not supported.')

    subprocess.run(
            ['git', 'clone', 'https://github.com/logan-britt/i3-config.git'])
    print()

    os.chdir('i3-config')
    subprocess.run(['python', 'install.py'])
    os.chdir('..')

def dwm(clean_up=False):
  pass

'''
  These functions pretain to the running of different internet types (tor),
  and different vpn setups to secure online communications. It runs line 
  every other set of config functions with a 
'''

def tor_setup(clean_up=False):
    print('Not configured yet...')

def vpn_setup(clean_up=False):
    if platform.system() == 'Linux':
        if 'arch' in platform.platform():
            subprocess.run(
                ['pacman', '-S', 'openvpn', 'networkmanager-openvpn'])

        elif 'ubuntu' in platform.platform():
            pass

        else:
            raise RuntimeError('This distro is not supported.')

    elif platform.system() == 'Darwin':
        pass

    elif platform.system() == 'Windows':
        pass

    else:
        raise RuntimeError('This operating system is not supported.')

'''
  This block of code runs the main function for this script. The first chunk
  of the code processes the user inputs and the second chunk of the code
  takes the user input and processes it into the 
'''

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
  pass
