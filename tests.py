#!/usr/bin/env python3
#
# Test for VideoSort post-processing script for NZBGet.
#
# Copyright (C) 2023 Denis <denis@nzbget.com>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with the program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
from os.path import dirname
import os
import traceback
import re
import shutil
import subprocess
import json
import getopt

POSTPROCESS_SUCCESS=93
POSTPROCESS_NONE=95
POSTPROCESS_ERROR=94

root_dir = dirname(__file__)
test_dir = root_dir + '/__'

def TEST(statement: str, test_func):
	print('\n********************************************************')
	print('TEST:', statement)
	print('--------------------------------------------------------\n')

	try:
		test_func()
		print('SUCCESS')
	except Exception as e:
		print(e)
		print(test_func.__name__, 'FAILED')
	finally:
		print('********************************************************\n')

def get_python(): 
	if os.name == 'nt':
		return 'python'
	return 'python3'

def run_script():
	sys.stdout.flush()
	proc = subprocess.Popen([get_python(), root_dir + './FakeDetector.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=os.environ.copy())
	out, err = proc.communicate()
	ret_code = proc.returncode
	return (out.decode(), int(ret_code), err.decode())

def set_defaults_env():
	# NZBGet global options
	os.environ['NZBOP_SCRIPTDIR'] = 'test'

	# script options
	os.environ['NZBPO_BANNEDEXTENSIONS'] = '.mkv,.mp4'

	# properties of nzb-file
	os.environ['NZBPP_DIRECTORY'] = test_dir
	os.environ['NZBPP_NZBNAME'] = 'test'
	os.environ['NZBPP_PARSTATUS'] = '2'
	os.environ['NZBPP_UNPACKSTATUS'] = '2'
	os.environ['NZBPP_CATEGORY'] = ''

	# pp-parameters of nzb-file, including DNZB-headers
	os.environ['NZBPR__DNZB_USENZBNAME'] = 'no'
	os.environ['NZBPR__DNZB_PROPERNAME'] = ''
	os.environ['NZBPR__DNZB_EPISODENAME'] = ''

	os.environ['NZBNA_EVENT'] = 'NZB_ADDED'
	os.environ['NZBOP_ARTICLECACHE'] = '64'

def TEST_COMPATIBALE_NZBGET_VERSION():
	os.environ['NZBNA_EVENT'] = ''
	os.environ['NZBPP_DIRECTORY'] = ''
	os.environ['NZBPO_BANNEDEXTENSIONS'] = ''
	res = run_script()
	assert('*** NZBGet queue script ***' in res[0])
	assert('This script is supposed to be called from nzbget (14.0 or later).' in res[0])
	assert(res[1] == 1)

def TEST_IGNORE_INCOMPATIBALE_EVENT():
	set_defaults_env()
	os.environ['NZBNA_EVENT'] = ''
	res = run_script()
	assert(res[1] == 0)


def RUN_TESTS():
	TEST('Should not be executed if nzbget version is incompatible', TEST_COMPATIBALE_NZBGET_VERSION)
	TEST('Should ignore incompatibale event', TEST_IGNORE_INCOMPATIBALE_EVENT)


RUN_TESTS()
