import os

homedir = os.path.expanduser("~")

class TestZsh:
  def test_zshrc(self):
    filename = '.zshrc'
    fqFilename = os.path.join(homedir,filename)
    assert os.path.exists(fqFilename) == True
    assert os.path.islink(fqFilename) == True

  def test_zshenv(self):
    filename = '.zshenv'
    fqFilename = os.path.join(homedir,filename)
    assert os.path.exists(fqFilename) == True
    assert os.path.islink(fqFilename) == True
