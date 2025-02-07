#!/usr/bin/env python
# Author: Zhang Yunjun, Nov 15, 2021


import pyaps3 as pa

print('------------------------------------------------')
print('import pyaps3 from {}'.format(pa.__file__))
print('------------------------------------------------')
print('test ERA5 data download')
print('NOTE: Account setup is required on the Copernicus Climate Data Store (CDS).')
print('      More detailed info can be found on: https://retostauffer.org/code/Download-ERA5/')
print('      Add your account info to ~/.cdsapirc file.')
pa.ECMWFdload(['20100601','20100901'], hr='14', filedir='./data/ERA5', model='ERA5', snwe=(30,40,120,140))

print('------------------------------------------------')
print('Downloads OK')
print('------------------------------------------------')
