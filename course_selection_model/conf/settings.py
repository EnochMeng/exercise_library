#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/7/4
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STUDENTDB_PATH = os.path.join(BASE_DIR, r'db\student')
TEACHERDB_PATH = os.path.join(BASE_DIR, r'db\teacher')
COURSE_PATH = os.path.join(BASE_DIR, r'db\course')
SCHOOL_PATH = os.path.join(BASE_DIR, r'db\school')
CLASS_PATH = os.path.join(BASE_DIR, r'db\class')

