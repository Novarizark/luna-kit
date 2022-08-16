#!/usr/bin/env python3


import os, sys
import lib

CWD=sys.path[0]

# controller config handler
cfg=lib.cfgparser.read_cfg(CWD+'/conf/setup.ini')
 
LUNA_ROOT= cfg['CONST']['luna_root']
DMDB_ROOT = cfg['CONST']['domdb_root']
CONST_ROOT=cfg['CONST']['const_root']

for itm in ['domaindb','luna']:
    try:
        os.remove(CWD+'/'+itm)
    except OSError:
        pass

os.system('ln -sf '+LUNA_ROOT+' ./luna')
os.system('ln -sf '+DMDB_ROOT+' ./domaindb')

try:
    os.remove(CWD+'/luna/DATA')
except OSError:
    pass

os.system('ln -sf '+CONST_ROOT+' ./luna/DATA')
