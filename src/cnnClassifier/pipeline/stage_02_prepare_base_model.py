from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger
import os

STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            # Ensure the output directory exists
            os.makedirs("artifacts/prepare_base_model", exist_ok=True)

            # Initialize ConfigurationManager to load the config
            config = ConfigurationManager()

            # Fetch the configuration for PrepareBaseModel
            prepare_base_model_config = config.get_prepare_base_model_config()

            # Initialize PrepareBaseModel with the configuration
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)

            # Call methods to get and update the base model
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()

            logger.info(f"{STAGE_NAME} completed successfully.")

        except Exception as e:
            logger.error(f"Error in {STAGE_NAME}: {e}")
            raise e

