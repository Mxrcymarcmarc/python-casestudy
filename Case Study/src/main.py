# main pipeline
#orchestrates pipeline: load config, ingest, transform, analyze, reports, timing.
# main.py

import json
import os
from typing import List, Dict, Any

# Import project modules
import ingest
import transform
import analyze
import reports


