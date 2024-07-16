import toml, pytest

@pytest.mark.it("numpy must exist on the Pipfile dependency [packages]")
def test_pipfile_contains_flask():
  with open("Pipfile", "r") as f:
    toml_content = f.read()
    parsed_toml = toml.loads(toml_content)
    keys = parsed_toml["packages"].keys()
    assert "numpy" in keys
