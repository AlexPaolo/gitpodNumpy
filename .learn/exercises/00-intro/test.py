import pytest, os
import numpy as np
from src.app import X

@pytest.mark.it("Folder src must exist")
def test_src_folder():
  assert os.path.isdir("./src/")

@pytest.mark.it("File src/app.py must exist")
def test_pipfile_exists():
  assert os.path.isfile("src/app.py")


@pytest.mark.it("Create a np array")
def test_declare_variable():
    assert X.shape == (4, 4)
    assert np.all(X == np.array([[ 2,  4,  6,  8],
                                 [10, 12, 14, 16],
                                 [18, 20, 22, 24],
                                 [26, 28, 30, 32]]))

