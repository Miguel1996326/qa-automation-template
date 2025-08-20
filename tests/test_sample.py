import pytest

@pytest.mark.smoke
def test_sample_smoke():
    # Test simple que siempre pasa
    assert 2 + 2 == 4
