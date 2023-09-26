# Nudity Detection with Google Cloud Vision API

## Overview
This Python script uses the Google Cloud Vision API to detect nudity in images. It classifies images into different levels of likelihood for containing adult content and optionally moves the files into corresponding folders based on their likelihood levels.

## Features
- Classifies images using Google Cloud Vision API's Safe Search Detection.
- Moves images into sub-folders based on their adult content likelihood level.
- Takes a folder path as an argument, and if not provided, defaults to the current directory.
- Creates necessary sub-folders for classification inside the path provided.

## Requirements
- Python 3.x
- `google-cloud-vision` Python package
- Google Cloud Platform account with Vision API enabled
- Google Cloud Service Account and corresponding JSON credentials file

## Installation

### Install Python Package Dependencies
Run the following command to install the required Python package:
```bash
pip install google-cloud-vision
```

### Set Up Google Cloud
1. Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the Vision API.
3. Create a service account and download the JSON credentials file.
4. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the JSON credentials file.
```bash
export GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
```

## Usage

### Basic Usage
Run the script without any arguments to process images in the `nude` sub-folder of the current directory:
```bash
python nudity_detection.py
```

### Specify Folder
Use the `--f` flag to specify a different folder to process:
```bash
python nudity_detection.py --f /path/to/folder
```

This will process the images in the `nude` sub-folder of the specified folder and create sub-folders for classification there.

## License
MIT License. See `LICENSE` file for details.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
