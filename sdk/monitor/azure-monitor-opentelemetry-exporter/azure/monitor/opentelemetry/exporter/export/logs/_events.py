# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from json import loads, dumps
from logging import LogRecord, getLogger, INFO

from opentelemetry.sdk._logs import LoggingHandler
from opentelemetry.util.types import Attributes


_APPLICATION_INSIGHTS_EVENT_MARKER_ATTRIBUTE = "APPLICATION_INSIGHTS_EVENT_MARKER_ATTRIBUTE"
_event_logger = getLogger(__name__)

# TODO: JEREVOSS: Consider a handler that ONLY adds the attribute and does not extend LoggingHandler. This would only work if the root handler is added too
class _AzureMonitorEventHandler(LoggingHandler):
    @staticmethod
    def _get_attributes(record: LogRecord) -> Attributes:
        attributes = LoggingHandler._get_attributes(record)
        attributes[_APPLICATION_INSIGHTS_EVENT_MARKER_ATTRIBUTE] = True
        return attributes

class _AzureMonitorEventTracker:
    _initialized = False
    def _initialize():
        if not _AzureMonitorEventTracker._initialized:
            _event_logger.addHandler(_AzureMonitorEventHandler())
            _event_logger.setLevel(INFO)
            _AzureMonitorEventTracker._initialized = True

def track_event(name: str, custom_dimensions: dict[str, str], custom_measurements: dict[str, float]):
    _AzureMonitorEventTracker._initialize()
    # _event_logger.info("test_event", extra={
    #     "a": {
    #         "aa": "aa",
    #         "ab": "ba",
    #     }
    # })
    custom_dimensions = dumps(custom_dimensions)
    custom_measurements = dumps(custom_measurements)
    _event_logger.info(name, extra={
        "customDimensions": custom_dimensions,
        "customMeasurements": custom_measurements
    })