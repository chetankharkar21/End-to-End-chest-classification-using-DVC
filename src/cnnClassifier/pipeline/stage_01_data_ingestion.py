from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info("Initializing ConfigurationManager...")
            config = ConfigurationManager()

            logger.info("Fetching DataIngestionConfig...")
            data_ingestion_config = config.get_data_ingestion_config()

            logger.info("Initializing DataIngestion...")
            data_ingestion = DataIngestion(config=data_ingestion_config)

            logger.info("Downloading file...")
            data_ingestion.download_file()

            logger.info("Extracting zip file...")
            data_ingestion.extract_zip_file()

            logger.info("Pipeline executed successfully!")
        except Exception as e:
            logger.error(f"Pipeline execution failed: {e}")
            raise RuntimeError(f"Pipeline execution failed due to: {str(e)}") from e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX===============X")
    except Exception as e:
        logger.exception(e)
        raise e

