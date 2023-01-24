import os, pytest

cwd = os.getcwd()
stowPath = '~'

def lsRecursive(lsRoot):
  return list(
    os.path.join(parent, name)
    for (parent, subdirs, files) in os.walk(lsRoot)
    for name in files + subdirs
  )

def pathExists(filename):
  fqFilename = os.path.expanduser(filename)
  return os.path.exists(fqFilename)

def pathIsLink(filename):
  fqFilename = os.path.expanduser(filename)
  return os.path.islink(fqFilename)

def pathIsDir(filename):
  fqFilename = os.path.expanduser(filename)
  return os.path.isdir(fqFilename)

class TestZsh:
  filesAll = list(map(lambda x: x.removeprefix('zsh/'), lsRecursive('zsh')))
  filesExist = list(['.zshrc', '.zshenv'])
  filesNoExist = [ x for x in filesAll if x not in list(['.zshrc', '.zshenv']) ]

  @pytest.mark.parametrize("filename", filesExist)
  @pytest.mark.parametrize("stowPath", stowPath)
  def test_exists(self, stowPath, filename):
    isLink = pathIsLink(os.path.join(stowPath, filename))
    isDir = pathIsDir(os.path.join(stowPath, filename))
    assert ( isLink or isDir ) == True

  @pytest.mark.parametrize("filename", filesNoExist)
  @pytest.mark.parametrize("stowPath", stowPath)
  def test_not_exist(self, stowPath, filename):
    assert not pathExists(os.path.join(stowPath, filename)) == True

class TestStarship:
  filesAll = list(map(lambda x: x.removeprefix('starship/'), lsRecursive('starship')))
  filesExist = list(['.config', '.config/starship.toml'])
  filesNoExist = [ x for x in filesAll if x not in list(['.config', '.config/starship.toml']) ]

  @pytest.mark.parametrize("filename", filesExist)
  @pytest.mark.parametrize("stowPath", stowPath)
  def test_exists(self, stowPath, filename):
    isLink = pathIsLink(os.path.join(stowPath, filename))
    isDir = pathIsDir(os.path.join(stowPath, filename))
    assert ( isLink or isDir ) == True

  @pytest.mark.parametrize("filename", filesNoExist)
  @pytest.mark.parametrize("stowPath", stowPath)
  def test_not_exist(self, stowPath, filename):
    assert not pathExists(os.path.join(stowPath, filename)) == True
