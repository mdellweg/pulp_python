import pytest

from pulp_python.app.utils import write_simple_index


def test_write_simple_index():
    project_names = ["aprojectname", "under_score", "da-sh"]
    page = write_simple_index(project_names)
    assert "aprojectname" in page
    assert "under-score" in page
    assert "da-sh" in page


@pytest.mark.parametrize(
    "name", ['<script lang="javascript">alert("Evil!")</script>', "gefährlich"]
)
def test_write_simple_index_rejects_invalid_package_name(name):
    project_names = [name]
    page = write_simple_index(project_names)
    assert name not in page
