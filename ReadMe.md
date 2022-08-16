# LUNA-KIT 

Control script pipeline for OTPSnc tide model run.

## Setup
First please edit `conf/setup.ini` according to your environment to setup static data and other parameters. Then run `setup.py` to link OTPSnc model and domaindb folder to this working directory.

## Usage

### Modify config.ini

When you properly setup the pipeline, to run the model either in series or matrix mode, first edit the `./conf/config.ini` file properly.

### Execute the pipeline
```bash
cd $LUNA_KIT_HOME
python3 run_series.py # run in series mode
python3 run_matrix.py # run in matrix mode
```

### run_series.py 
The main control script to run model according to prescribed sites in `[SERIES][site_file]`.

### run_matrix.py
The main control script to run model according to prescribed domain in `[MATRIX][domain_file]`.
Output style example:
``` python
netcdf njord_his_d01.20100721 {
dimensions:
	xi_rho = 770 ;
	eta_rho = 514 ;
	ocean_time = UNLIMITED ; // (25 currently)
variables:
	double lon_rho(eta_rho, xi_rho) ;
		lon_rho:long_name = "longitude of RHO-points" ;
		lon_rho:units = "degree_east" ;
		lon_rho:standard_name = "longitude" ;
		lon_rho:field = "lon_rho, scalar" ;
	double lat_rho(eta_rho, xi_rho) ;
		lat_rho:long_name = "latitude of RHO-points" ;
		lat_rho:units = "degree_north" ;
		lat_rho:standard_name = "latitude" ;
		lat_rho:field = "lat_rho, scalar" ;
	float tide_z(ocean_time, eta_rho, xi_rho) ;
		zetaw:long_name = "Tide-caused sea level anomaly" ;
		zetaw:units = "meter" ;
		zetaw:time = "ocean_time" ;
		zetaw:grid = "grid" ;
		zetaw:location = "face" ;
		zetaw:coordinates = "lon_rho lat_rho ocean_time" ;
		zetaw:_FillValue = 1.e+37f ;
```

Zhenning LI
Aug 17, 2022

