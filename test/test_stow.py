import os, pytest

cwd = os.getcwd()
stowPath = '~'

def pathExists(filename):
  fqFilename = os.path.expanduser(filename)
  return os.path.exists(fqFilename)

def pathIsLink(filename):
  fqFilename = os.path.expanduser(filename)
  return os.path.islink(fqFilename)

class TestZsh:
  filesExist = [ '.zshrc', '.zshenv' ]
  filesNoExist = os.listdir(os.path.join(cwd,'zsh'))
  for filename in filesExist:
    filesNoExist.remove(filename)

  @pytest.mark.parametrize("filename", filesExist)
  @pytest.mark.parametrize("stowPath", stowPath)
  def test_exists(self, stowPath, filename):
    assert pathIsLink(os.path.join(stowPath, filename)) == True

  @pytest.mark.parametrize("filename", filesNoExist)
  @pytest.mark.parametrize("stowPath", stowPath)
  def test_not_exist(self, stowPath, filename):
    assert not pathExists(os.path.join(stowPath, filename)) == True
