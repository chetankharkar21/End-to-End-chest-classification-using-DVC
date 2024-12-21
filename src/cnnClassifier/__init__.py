import os
import sys
import logging

# Logging format string with correct variable names
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Log directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Log level for capturing events (INFO, DEBUG, etc.)
    format=logging_str,  # Custom log format
    handlers=[
        logging.FileHandler(log_filepath),  # Logs to a file
        logging.StreamHandler(sys.stdout)   # Logs to console
    ]
)

# Create a logger instance
logger = logging.getLogger("cnnClassifierLogger")

# Example usage of logger
'''logger.info("Logger is set up and working.")
logger.error("This is an error message.")''' 
