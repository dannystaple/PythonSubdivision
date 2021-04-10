"""
What this whole experiment was working up to.
The intent:
Given an image, and a threshold of intensity,
continue subdividing while regions contain more than one intensity.
"""
import json
import sys


def convert_region(region, threshold):
    """Given a pil image region,
    if it can be subdivided, and the intensity extrema > threshold,
        then convert the subdivisions
    or return an empty region"""
    width, height = region.size
    if width > 1 and height > 1:
        a, b = region.getextrema()
        print(repr(a), repr(b))
        if abs(a - b) >= threshold:
            #subdivide and convert each - using region.crop
            hwidth = width / 2
            hheight = height / 2
            return [
                convert_region(region.crop([0, 0, hwidth, hheight]), threshold),
                convert_region(region.crop([hwidth, 0, width, hheight]), threshold),
                convert_region(region.crop([0, hheight, hwidth, height]), threshold),
                convert_region(region.crop([hwidth, hheight, width, height]), threshold)
            ]
    return []


def convert_image(image_data, threshold):
    return convert_region(image_data, threshold)


def main():
    image_filename, subdiv_output_filename = sys.argv[1:]
    #Greyscale differences of less than 20 will be ignored
    threshold = 2
    #Note - we use intensity - so convert to greyscale first.
    from PIL import Image
    image_data = Image.open(image_filename).convert("L")
    subdiv_data = convert_image(image_data, threshold)
    with open(subdiv_output_filename, "w") as fd:
        json.dump(subdiv_data, fd)


if __name__ == "__main__":
    main()
