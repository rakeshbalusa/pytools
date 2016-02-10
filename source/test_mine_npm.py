#
#  Copyright (c) 2015 nexB Inc. and others. All rights reserved.
#

from __future__ import absolute_import, print_function

import os

from commoncode.testcase import FileBasedTesting

from spats import mine_npm


class TestAnalyzeRepoData(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_get_npm_packages(self):
        expected = 'amulet'
        test_file = self.get_test_loc('mine-npm/amulet.json')
        output = mine_npm.get_npm_packages(test_file)
        assert expected == output[0].name
        assert '1.0.4' == output[0].version
        assert 'https://github.com/chbrown/amulet' == output[0].homepage_url
        assert 'amulet@1.0.4' == output[0].id

    def test_get_npm_names(self):
        expected = [
            u'an-ansi',
            u'amznjp-url-normalize',
            u'amzn-papi',
            u'an-array',
            u'amz-products',
            u'amusic',
            u'an',
            u'amulet',
            u'amx',
            u'amz',
            u'amvn',
            u'amygdala'
            ]
        test_file = self.get_test_loc('mine-npm/names.json')
        output = mine_npm.get_npm_names(test_file)
        assert expected == output
