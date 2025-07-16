# BioLinkRemoverBot - All rights reserved
# --------------------------------------
# This code is fully owned by BioLinkRemoverBot and is reserved.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log(message):
    """Logs important events and errors."""
    logging.info(message)

def error_log(error_message):
    """Logs error events."""
    logging.error(error_message)
