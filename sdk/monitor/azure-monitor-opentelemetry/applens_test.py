# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

import logging
import threading
from os import makedirs
from os.path import exists, join

from azure.monitor.opentelemetry._constants import (
    _get_log_path,
)

_DIAGNOSTIC_LOGGER_FILE_NAME = "applicationinsights-extension.log"
_logger = logging.getLogger(__name__)
# _logger.propagate = False
_logger.setLevel(logging.DEBUG)
_DIAGNOSTIC_LOG_PATH = _get_log_path()
_ATTACH_SUCCESS_DISTRO = "4200"
_ATTACH_SUCCESS_CONFIGURATOR = "4201"
_ATTACH_FAILURE_DISTRO = "4400"
_ATTACH_FAILURE_CONFIGURATOR = "4401"



log_format = (
    "{"
    + '"time":"%(asctime)s.%(msecs)03d", '
    + '"level":"%(levelname)s", '
    + '"logger":"%(name)s", '
    + '"message":"%(message)s", '
    + '"properties":{'
    + '"operation":"Startup", '
    + '"language":"python"'
    + "}"
    + "}"
)
if not exists(_DIAGNOSTIC_LOG_PATH):
    makedirs(_DIAGNOSTIC_LOG_PATH)
f_handler = logging.FileHandler(
    join(
        _DIAGNOSTIC_LOG_PATH, "TEST" + _DIAGNOSTIC_LOGGER_FILE_NAME
    )
)
formatter = logging.Formatter(
    fmt=log_format, datefmt="%Y-%m-%dT%H:%M:%S"
)
f_handler.setFormatter(formatter)
_logger.addHandler(f_handler)

_logger.info("info")
_logger.warning("warning")
_logger.error("error")

############################################################

from json import dumps
from os import makedirs
from os.path import exists, join

from azure.monitor.opentelemetry._constants import (
    _get_log_path,
)

_STATUS_LOG_PATH = _get_log_path(status_log_path=True)

status_json = "blah"
if not exists(_STATUS_LOG_PATH):
    makedirs(_STATUS_LOG_PATH)
# Change to be hostname and pid
status_logger_file_name = "status_logger_file_name"
with open(
    join(_STATUS_LOG_PATH, status_logger_file_name),
    "w",
    encoding="utf8"
) as f:
    f.seek(0)
    f.write(dumps(status_json))
    f.truncate()
