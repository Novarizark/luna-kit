#!/usr/bin/env python3
'''
Date: Aug 16, 2022
Control Tide model run in series mode  
Revision:
Mar 7, 2022 --- Initial
Aug 16, 2022 --- Modify for luna-kit 
'''

import logging.config
import pandas as pd
import xarray as xr
import datetime
import os, sys, lib
from utils import utils

CWD=sys.path[0]

def main():
    # logging manager
    logging.config.fileConfig('./conf/logging_config.ini')

    utils.write_log('Read Config...')    
    # controller config handler
    cfg=lib.cfgparser.read_cfg('./conf/config.ini')

    if cfg['BASIC']['model_init_ts']=='realtime':
        strt_time=datetime.datetime.today()
        strt_time=strt_time.replace(
            hour=0,minute=0,second=0,microsecond=0)
    else:
        strt_time=datetime.datetime.strptime(
            cfg['BASIC']['model_init_ts'], '%Y%m%d%H')

    fcst_days=int(cfg['BASIC']['model_run_days'])
    
    arch_dir=cfg['ARCH']['arch_root']+'/'+cfg['BASIC']['model_init_ts']
    df_tf=pd.date_range(strt_time, periods=fcst_days*24+1, freq='H')
    
    # read domain data
    ds_dom=xr.open_dataset(cfg['MATRIX']['domain_file'])
    lat2d=ds_dom['lat_rho'].values
    lon2d=ds_dom['lon_rho'].values
    mask=ds_dom['mask_rho'].values

    if not(os.path.exists('luna')):
        utils.throw_error(
            'luna directory not found, please setup first')


    # -------------------MODIFY THE FOLLOWING-------------------
    # write OTPS needed input file
    with open(CWD+'/luna/site_input', 'w') as f:
        for site in df_sites.iterrows():
            lat=site[1]['lat']
            lon=site[1]['lon']
            for tf in df_tf:
                str=('%10.4f%10.4f%6d%4d%4d%4d%4d%4d' % (
                    lat, lon, tf.year, tf.month, tf.day, 
                    tf.hour, tf.minute, tf.second))
                f.write(str+'\n')
    utils.write_log('Luna model run...')
    # run OTPS
    os.system('cd %s/luna;./predict_tide<setup.inp' % CWD)
    # read output
    # write log

    if not os.path.exists(arch_dir):
        os.mkdir(arch_dir)

    os.system('mv %s/luna/z.out %s/tides.%s' % (
        CWD, arch_dir, strt_time.strftime('%Y%m%d%H')))

if __name__=='__main__':
    main()
