import logging
import os
from datetime import datetime

# Define the log file name based on the current datetime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Define the directory where logs will be saved
logs_dir = os.path.join(os.getcwd(), "logs")
# Create the directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# if __name__ == "__main__":
#     logging.info("Logging has Started")