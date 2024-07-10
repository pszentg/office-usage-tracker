import os


class Config:
    LOG_LEVEL = "INFO"
    TASK_1_OUTPUT = "/output/first.csv"
    TASK_2_OUTPUT = "/output/second.csv"
    SOURCES_ROOT = os.path.dirname(__file__)
    RESOURCES_ROOT = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "resources"
    )

    # ISO-8601 format
    TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
