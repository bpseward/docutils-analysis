#! /usr/bin/env python

# $Id: test___init__.py 8356 2019-08-26 16:44:19Z milde $
# Author: Lea Wiemann <LeWiemann@gmail.com>
# Copyright: This module has been placed in the public domain.

"""
Test module for transforms/__init__.py.
"""
from __future__ import absolute_import

import unittest

from . import DocutilsTestSupport # must be imported before docutils
from docutils import transforms, utils


class TestTransform(transforms.Transform):

    default_priority = 100

    applied = 0
    
    def apply(self, **kwargs):
        self.applied += 1
        assert kwargs == {'foo': 42}


class KwargsTestCase(unittest.TestCase):

    def test_kwargs(self):
        transformer = transforms.Transformer(utils.new_document('test data'))
        transformer.add_transform(TestTransform, foo=42)
        transformer.apply_transforms()
        self.assertEqual(len(transformer.applied), 1)
        self.assertEqual(len(transformer.applied[0]), 4)
        transform_record = transformer.applied[0]
        self.assertEqual(transform_record[1], TestTransform)
        self.assertEqual(transform_record[3], {'foo': 42})


if __name__ == '__main__':
    unittest.main()
