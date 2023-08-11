# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import logging

from opentelemetry.sdk._logs import LoggingHandler
from opentelemetry.util.types import Attributes


_APPLICATION_INSIGHTS_EVENT_MARKER_ATTRIBUTE = "APPLICATION_INSIGHTS_EVENT_MARKER_ATTRIBUTE"


class AzureMonitorEventHandler(LoggingHandler):
    @staticmethod
    def _get_attributes(record: logging.LogRecord) -> Attributes:
        attributes = LoggingHandler._get_attributes(record)
        attributes[_APPLICATION_INSIGHTS_EVENT_MARKER_ATTRIBUTE] = True
        return attributes