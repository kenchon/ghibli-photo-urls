import json

"""
Script to make URL list of Ghibli screenshot images
"""

def get_titlewise_url_list(base_url, title):
    """
    get title-wise image url list
    e.g url_list = [http://www.ghibli.jp/gallery/ponyo001.jpg,...]
    """
    url_list = list(
        map(lambda number: f'{base_url}/{title}{number+1:03}.jpg', list(range(50)))
    )
    return url_list

if __name__ == "__main__":

    # Filepath to save
    output_filepath = './ghibli-images.json'

    # Ghibli-specific values
    base_url = 'http://www.ghibli.jp/gallery'
    title_list = [
        'ponyo',
        'kazetachinu',
        'chihiro',
        'kaguyahime',
        'marnie',
        'kokurikozaka',
        'karigurashi',
        'ged',
    ]
    ghibli_images_dict = {}

    for title in title_list:
        full_url_list = get_titlewise_url_list(base_url, title)
        ghibli_images_dict[title] = full_url_list

    # Save dict as json
    with open(output_filepath, 'w') as output_file:
        json.dump(ghibli_images_dict, output_file, indent=4)
