import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: 'DataIngestionConfig'):
        self.config = config

    def download_file(self) -> str:
        """
        Fetch data from the URL and save it locally as a zip file.
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file

            # Create the parent directory for the zip file if it doesn't exist
            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)

            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            # Correcting the prefix for Google Drive file download
        
            file_url = 'https://drive.google.com/uc?id=11JqNDxjF-pQC_jGXDwWG0djAGJGHkdNs&export=download'
            
            # Downloading the file using gdown
            gdown.download(file_url, zip_download_dir, quiet=False)  # Set quiet=False for detailed logs

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            logger.error(f"Error occurred while downloading file: {e}")
            raise e

    def extract_zip_file(self):
        """
        Extracts the zip file into the specified directory.
        """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)

            # Extracting the zip file
            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)
            
            logger.info(f"Extracted zip file {self.config.local_data_file} into directory {unzip_path}")
        except zipfile.BadZipFile as e:
            logger.error(f"Invalid zip file: {e}")
            raise e
        except FileNotFoundError as e:
            logger.error(f"Zip file not found: {e}")
            raise e
        except Exception as e:
            logger.error(f"Error occurred while extracting zip file: {e}")
            raise e