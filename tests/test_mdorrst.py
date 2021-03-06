#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mdorrst
----------------------------------

Tests for `mdorrst` module.
"""

import os
import glob
import pytest

from mdorrst import sniff

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'readmes/',
)


@pytest.mark.parametrize(
    "readme_file,readme_style",
    [(readme_file, readme_file.split('.')[-1]) for
     readme_file in
     glob.glob(os.path.join(FIXTURE_DIR, '*/*/README.*'))])
def test_files(readme_file, readme_style):
    with open(readme_file) as readme:
        assert sniff(readme.read()) == readme_style
