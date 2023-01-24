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

def buildLists(dir,filesExist):
  filesAll = list(map(lambda x: x.removeprefix(dir), lsRecursive(dir)))
  filesNoExist = [ x for x in filesAll if x not in filesExist ]
  return filesExist, filesNoExist

class TestZsh:
  filesExist, filesNoExist = buildLists('zsh', [ '.zshrc', '.zshenv' ])

  @pytest.mark.parametrize("filename", filesExist)
  def test_exists(self, filename):
    isLink = pathIsLink(os.path.join(stowPath, filename))
    isDir = pathIsDir(os.path.join(stowPath, filename))
    assert ( isLink or isDir ) == True

  @pytest.mark.parametrize("filename", filesNoExist)
  def test_not_exist(self, filename):
    assert not pathExists(os.path.join(stowPath, filename)) == True

class TestStarship:
  filesExist, filesNoExist = buildLists('starship', ['.config', '.config/starship.toml'])

  @pytest.mark.parametrize("filename", filesExist)
  def test_exists(self, filename):
    isLink = pathIsLink(os.path.join(stowPath, filename))
    isDir = pathIsDir(os.path.join(stowPath, filename))
    assert ( isLink or isDir ) == True

  @pytest.mark.parametrize("filename", filesNoExist)
  def test_not_exist(self, filename):
    assert not pathExists(os.path.join(stowPath, filename)) == True
