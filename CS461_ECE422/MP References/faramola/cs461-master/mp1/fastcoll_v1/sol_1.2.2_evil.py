#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            mM�vՐ0��佷�Y�a��Mi�S�8������j���d�s���:;6�tP��f-�(,�3��B$/��߯�����M�F.��Z~���o�l������h�M���,%)��Q �A�M���6�"""
from hashlib import sha256
if(sha256(blob).hexdigest()[-1] == 'c'):
	print "I come in peace."
else:
	print "Prepare to be destroyed!"