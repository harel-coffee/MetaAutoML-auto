import os
from JsonUtil import get_config_property


def in_cluster() -> bool:
    return get_config_property("env-varname-cluster") in os.environ