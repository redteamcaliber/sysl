from src.sysl import syslloader, sysldata
import unittest
import re, os, sys

import traceback

import argparse as ap

class TestSetOf(unittest.TestCase):

  def test_set_of(self):

    try:
      (module, _, _) = syslloader.load('/test/data/test_data', True, '.')

      d = {
        'project' : 'TestData :: Data Views',
        'output'  : 'test_set_of-data.png',
        'plantuml': '',
        'verbose' : '',
        'filter'  : None,
      }
      args = ap.Namespace(**d)

      out = sysldata.dataviews(module, args)

      self.assertTrue(
        re.search(r'(?ms)^class "Type1" as _1 .*^_0  \*-- "0..\*" _1', out[0])
        or
        re.search(r'(?ms)^class "Type1" as _0 .*^_1  \*-- "0..\*" _0', out[0]),
        out[0])

    except (IOError, Exception) as e:
      self.fail(traceback.format_exc())

if __name__ == '__main__':
  unittest.main()
