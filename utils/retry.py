
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)

from google.api_core.exceptions import (
    ResourceExhausted,
    ServiceUnavailable,
    DeadlineExceeded
)

import requests


def retry_agent(max_attempts=3):

    return retry(
        stop=stop_after_attempt(max_attempts),

        wait=wait_exponential(
            multiplier=1,
            min=1,
            max=5
        ),

        retry=retry_if_exception_type(
            (
                ResourceExhausted,
                ServiceUnavailable,
                DeadlineExceeded,
                requests.exceptions.Timeout,
                requests.exceptions.ConnectionError,
                TimeoutError
            )
        ),

        reraise=True
    )
