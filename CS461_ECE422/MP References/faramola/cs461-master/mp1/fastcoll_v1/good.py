#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           4$��,�����K~5Պ��Y�ӂo>�@"Mĥ�r��޳��oj���5��S��]{[r�q�&ȖC�P��.eI�X������cAz&/�l���KP���'��F�7ؑoy;��p��$[��6�LrE��="""
from hashlib import sha256
if(int(sha256(blob).hexdigest(), 16) % 2):
	print "I come in peace."
else:
	print "Prepare to be destroyed!"
