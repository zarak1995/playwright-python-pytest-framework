
import pytest


@pytest.mark.parametrize(
    "username",
    ["standard_user", "locked_out_user", "problem_user"]
)
def test_username(username):

    print(f"\nTesting username: {username}")

    assert username != ""
