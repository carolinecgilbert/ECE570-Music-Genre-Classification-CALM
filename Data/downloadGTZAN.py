import gdown

# Download dataset from Google Drive (will be saved in Data/Dataset as train_dataset.pt and test_dataset.pt)
url="https://drive.google.com/drive/folders/1S5tsxSqbR8hWdNfLrO_oLtBbJfHk9ERZ?usp=drive_link"
gdown.download_folder(url)