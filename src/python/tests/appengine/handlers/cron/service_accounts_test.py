# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for service_accounts.py"""

import unittest

from handlers.cron import service_accounts


class ServiceAccountIdTest(unittest.TestCase):
  """Tests _service_account_id."""

  def test_min_length(self):
    self.assertEqual(service_accounts._service_account_id('a'), 'bot-a0')

  def test_regular_length(self):
    self.assertEqual(service_accounts._service_account_id('abc'), 'bot-abc')

  def test_max_length(self):
    self.assertEqual(
        service_accounts._service_account_id('a' * 26), 'bot-%s' % ('a' * 26))

  def test_more_than_max_length(self):
    with self.assertRaises(AssertionError):
      service_accounts._service_account_id('a' * 27)