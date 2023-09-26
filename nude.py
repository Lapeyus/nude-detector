import os
import argparse
from google.cloud import vision
import shutil
from pathlib import Path

# Setting up the Google Cloud Platform credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'


# Initialize the Vision API client once to reuse
client = vision.ImageAnnotatorClient()


def check_nudity(image_path, destination_folder, move_files=False):
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response = client.safe_search_detection(image=image)
    safe = response.safe_search_annotation

    likelihood_mapping = {
        vision.Likelihood.VERY_UNLIKELY: 'very_unlikely',
        vision.Likelihood.UNLIKELY: 'unlikely',
        vision.Likelihood.POSSIBLE: 'possible',
        vision.Likelihood.LIKELY: 'likely',
        vision.Likelihood.VERY_LIKELY: 'very_likely'
    }

    level = likelihood_mapping.get(safe.adult, 'unknown')

    if move_files:
        dest_path = os.path.join(destination_folder, level, os.path.basename(image_path))
        shutil.move(image_path, dest_path)

    return level


def create_dirs(base_path):
    for dir_name in ['very_unlikely', 'unlikely', 'possible', 'likely', 'very_likely']:
        dir_path = os.path.join(base_path, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


def main():
    parser = argparse.ArgumentParser(description='Check images for nudity.')
    parser.add_argument('--f', type=str, default='.', help='The folder to process')
    args = parser.parse_args()

    base_path = args.f

    create_dirs(base_path)

    image_folder_path = Path(base_path)
    image_paths = [os.path.join(image_folder_path, name) for name in os.listdir(image_folder_path)]

    for image_path in image_paths:
        if os.path.isfile(image_path):
            adult_content_level = check_nudity(image_path, base_path, move_files=True)
            print(f'{os.path.basename(image_path)}: {adult_content_level}')


if __name__ == '__main__':
    main()
