# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""
Deprecated - module auditdextract.py has moved.

See :py:mod:`msticpy.analysis.data.auditdextract`
"""
import warnings
from .._version import VERSION

__version__ = VERSION
__author__ = "Pete Bryan"


# flake8: noqa: F403, F401
# pylint: disable=wildcard-import, unused-wildcard-import, unused-import
from ..analysis.data.auditdextract import *

WARN_MSSG = (
    "This module has moved to msticpy.analysis.data.auditdextract\n"
    "Please change your import to reflect this new location."
    "This will be removed in MSTICPy v2.0.0"
)
warnings.warn(WARN_MSSG, category=DeprecationWarning)
