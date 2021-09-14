"""Test conversion from images"""
import mock
from make_subdiv_from_image import convert_region


def test_single_pixel_region_should_make_empty_list():
    """Test with a single pixel region.
    The result should be a single empty list"""
    image = mock.Mock(size=(1, 1))
    assert convert_region(image, 2) == []


def test_with_region_of_one_colour_should_make_empty_list():
    """Given a region with only 1 colour, only an empty list should be produced - no boundaries"""
    region = mock.Mock(size=(1, 1))
    image = mock.Mock(size=(2, 2))
    image.crop.return_value = region
    image.getextrema.return_value = (1, 1)
    region.getextrema = image.getextrema
    assert convert_region(image, 2) == []

