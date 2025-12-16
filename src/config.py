import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RHUMBIX_API_KEY")
BASE_URL = os.getenv("RHUMBIX_BASE_URL")
