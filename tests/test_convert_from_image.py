"""Test conversion from images"""
import mock


def test_single_pixel_region_should_make_empty_list():
    """Test with a single pixel region.
    The result should be a single empty list"""
    image = mock.Mock()
    image.size = (1, 1)
    assert convert_region(image, 20) == []


