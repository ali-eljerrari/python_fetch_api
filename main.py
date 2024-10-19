import requests
from requests.exceptions import RequestException
import sys
import os

def fetch_random_dog_image():
    """Fetch a random dog image URL from the Dog CEO API."""
    url = 'https://dog.ceo/api/breeds/image/random'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        status = data.get('status')
        image_url = data.get('message')
        if status == 'success' and image_url:
            return image_url
        else:
            print('Error: API request failed.')
            return None
    except RequestException as e:
        print(f'An error occurred while making the request: {e}')
        return None
    except ValueError as e:
        print(f'Error parsing JSON response: {e}')
        return None

def download_image(image_url, save_directory='images'):
    """Download an image from a given URL and save it to a directory."""
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image_filename = os.path.basename(image_url)
        os.makedirs(save_directory, exist_ok=True)
        file_path = os.path.join(save_directory, image_filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f'Image saved as {file_path}')
    except RequestException as e:
        print(f'An error occurred while downloading the image: {e}')

def main():
    """Main function to fetch and download random dog images."""
    num_images = 1
    if len(sys.argv) > 1:
        try:
            num_images = int(sys.argv[1])
        except ValueError:
            print('Invalid number of images specified. Using default of 1.')
    for _ in range(num_images):
        print('Fetching random dog image URL...')
        image_url = fetch_random_dog_image()
        if image_url:
            print(f'Dog image URL: {image_url}')
            download_image(image_url)
        else:
            print('Failed to fetch dog image URL.')

if __name__ == '__main__':
    main()
