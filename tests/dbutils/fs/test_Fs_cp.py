import pytest

from python_databricks_env.dbutils.fs.Fs import Fs

fs = Fs()


def test_cp__file__source_not_exists(tmp_path):
    source = tmp_path / "source"

    assert not source.exists()

    target = tmp_path / "target"

    with pytest.raises(Exception):
        fs.cp(str(source), str(target))


def test_cp__file__norecurse(tmp_path):
    source = tmp_path / "source"
    source.touch()

    assert source.exists()

    target = tmp_path / "target"

    success = fs.cp(str(source), str(target))

    assert success
    assert source.exists()
    assert target.exists()


def test_cp__file__recurse_true(tmp_path):
    source = tmp_path / "source"
    source.touch()

    assert source.exists()

    target = tmp_path / "target"

    success = fs.cp(str(source), str(target), True)

    assert success
    assert source.exists()
    assert target.exists()


def test_cp__file__target_exists(tmp_path):
    source = tmp_path / "source"
    source.touch()

    assert source.exists()

    target = tmp_path / "target"
    target.touch()

    success = fs.cp(str(source), str(target))

    assert success
    assert source.exists()
    assert target.exists()


def test_cp__dir__source_not_exists(tmp_path):
    source = tmp_path / "source"

    assert not source.exists()

    target = tmp_path / "target"

    with pytest.raises(Exception):
        fs.cp(str(source), str(target), True)

def test_cp__dir__norecurse(tmp_path):
    source = tmp_path / "source"
    source.mkdir()

    assert source.exists()

    target = tmp_path / "target"

    with pytest.raises(Exception):
        fs.cp(str(source), str(target))


def test_cp__dir__recurse_true(tmp_path):
    source = tmp_path / "source"
    source.mkdir()

    assert source.exists()

    target = tmp_path / "target"

    success = fs.cp(str(source), str(target), True)

    assert success
    assert source.exists()
    assert target.exists()


def test_cp__dir__target_exists(tmp_path):
    source = tmp_path / "source"
    source.mkdir()

    assert source.exists()

    target = tmp_path / "target"
    target.mkdir()

    success = fs.cp(str(source), str(target), True)

    assert success
    assert source.exists()
    assert target.exists()
