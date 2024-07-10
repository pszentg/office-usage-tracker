import os


class Config:
    LOG_LEVEL = "INFO"
    SOURCES_PATH = os.path.dirname(__file__)
    RESOURCES_PATH = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "resources"
    )
    OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "output")

    # ISO-8601 format
    TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
