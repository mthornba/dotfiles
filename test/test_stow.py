import os

cwd = os.getcwd()

def pathExists(filename):
  fqFilename = os.path.expanduser(filename)
  return os.path.exists(fqFilename)

def pathIsLink(filename):
  fqFilename = os.path.expanduser(filename)
  return os.path.islink(fqFilename)

class TestZsh:
  def test_zshrc(self):
    assert pathIsLink('~/.zshrc') == True

  def test_zshenv(self):
    filename = '~/.zshenv'
    assert pathIsLink(filename) == True

  def test_not_exist(self):
    stowPath = '~'
    filesExist = [ '.zshrc', '.zshenv' ]
    filesNoExist = os.listdir(os.path.join(cwd,'zsh'))
    for file in filesExist:
      filesNoExist.remove(file)

    for filename in filesNoExist:
      assert not pathExists(os.path.join(stowPath, filename)) == True
