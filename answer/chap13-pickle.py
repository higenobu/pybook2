#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import os
list_data=['a','b','c']
ll=pickle.dumps(list_data)
print (ll)
list_again=pickle.loads(ll)
print (list_again)
