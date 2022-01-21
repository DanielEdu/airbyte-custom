#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_servicesnow_api import SourceServicesnowApi

if __name__ == "__main__":
    source = SourceServicesnowApi()
    launch(source, sys.argv[1:])
