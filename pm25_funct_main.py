#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################################################
# import libraries

import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as np
from mpl_toolkits.basemap import Basemap , cm
from osgeo import gdal, gdal_array, osr , ogr
import time

###################################################
# define functions that calculate concentrations of pollutants

def function_co ( domain_rows , domain_cols , lay , cmaq_data ):  # the order of argumenrs is important when input.

	data_mesh = np.empty( shape=( domain_rows , domain_cols ) )
	# start CMAQ algorithm
	for row in range(0,domain_rows,1):
		print('----------------------')
		print('-> loop for row= %s' %row)

		for col in range(0, domain_cols,1):
			#print('--------------------------------------')
			#print('loop for row=%s col=%s time-step=%s' %(row,col,tstep))
			cell_24hr_aconc = []
			# extract all 24 t-step
			cell_24hr_aconc = cmaq_data[ : , lay , row , col ]
			# change daily list to daily npArray
			cell_24hr_array = np.array( cell_24hr_aconc )
			# get the mean for the cell
			cell_mean = cell_24hr_array.mean()
			# pin daily mean to data mesh
			data_mesh[row][col] = cell_mean
			# delete daily list
			del cell_24hr_aconc

	return data_mesh
	
# each function reads its own files inside the function and writes out the data-mesh array

def function_pm25_monthly_mean ( days_in_month , domain_rows , domain_cols , lay) :

	print('-> month of analysis is=' , cmaq_file_month)

	pm25_mesh = np.ndarray( shape=(days_in_month , domain_rows , domain_cols) )
	# create a list in a range, use an argument-unpacking operator * to unpack the list
	day_list = [*range( 1 , days_in_month+1 , 1)] # don't forget the [] around range function to create the list

	for day_of_the_month in day_list :

		print('-> we are analyzing the follwoing days:')
		print(day_list)
		print( '-> calculating for day= %s' %day_of_the_month )
		# prepare the count days
		if day_of_the_month <= 9 :
			# if jday is less than 10, add zero before it
			day_count = '0'+str(day_of_the_month)

		else:
			# if jday is bigger than 9, use it.
			day_count = str(day_of_the_month)

		file_date_tag = '2016'+cmaq_file_month+day_count
		# setting the input files
		aconc_file_name = 'CCTM_ACONC_v52_CA_WRF_1km_griddedAgBioNonptPtfire_scen'+Landis_scenario+'_mpi_standard_'+file_date_tag+'.nc'
		
		pmdiag_file_name = 'CCTM_PMDIAG_v52_CA_WRF_1km_griddedAgBioNonptPtfire_scen'+Landis_scenario+'_mpi_standard_'+file_date_tag+'.nc'

		print('-> reading CMAQ files:')
		print( aconc_file_name )
		print( pmdiag_file_name )
		# set input directory
		input_dir = '/Users/ehsan/Documents/Python_projects/CMAQ_analysis/cmaq_inputs/' #'/storage/ehsanm/USFS_CA_WRF_1km/plots/'
		# define input files
		aconc_input = input_dir + aconc_file_name

		pmdiag_input = input_dir + pmdiag_file_name
		# read in cmaq and pmdiag input files
		aconc_in = Dataset( aconc_input , 'r' )
		pmdiag_in = Dataset( pmdiag_input , 'r')

		# read each cell in the C-storing style: row and then col
		for row in range( 0 , domain_rows , 1 ):

			for col in range( 0 , domain_cols , 1 ):

				print( f'-> processing row= {row} and col= {col}' )

				# loop inside 24 time-steps and extract pm cons
				# extract PM2.5 species from input files
				print('-> extracting species from CMAQ files...')
				# species from aconc [1]
				AH3OPI = aconc_in.variables['AH3OPI'][:,lay,row,col]
				AH3OPI = np.array(AH3OPI).mean()

				AH3OPJ = aconc_in.variables['AH3OPJ'][:,lay,row,col]
				AH3OPJ = np.array(AH3OPJ).mean()

				AH3OPK = aconc_in.variables['AH3OPK'][:,lay,row,col]
				AH3OPK = np.array(AH3OPK).mean()

				ACLI = aconc_in.variables['ACLI'][:,lay,row,col]
				ACLI = np.array(ACLI).mean()

				ACLJ = aconc_in.variables['ACLJ'][:,lay,row,col]
				ACLJ = np.array(ACLJ).mean()

				ACLK = aconc_in.variables['ACLK'][:,lay,row,col]
				ACLK = np.array(ACLK).mean()

				AECI = aconc_in.variables['AECI'][:,lay,row,col]
				AECI = np.array(AECI).mean()

				AECJ = aconc_in.variables['AECJ'][:,lay,row,col]
				AECJ = np.array(AECJ).mean()

				ANAI = aconc_in.variables['ANAI'][:,lay,row,col]
				ANAI = np.array(ANAI).mean()

				ANAJ = aconc_in.variables['ANAJ'][:,lay,row,col]
				ANAJ = np.array(ANAJ).mean()

				AMGJ = aconc_in.variables['AMGJ'][:,lay,row,col]
				AMGJ = np.array(AMGJ).mean()

				AKJ = aconc_in.variables['AKJ'][:,lay,row,col]
				AKJ = np.array(AKJ).mean()

				ACAJ = aconc_in.variables['ACAJ'][:,lay,row,col]
				ACAJ = np.array(ACAJ).mean()

				ANH4I = aconc_in.variables['ANH4I'][:,lay,row,col]
				ANH4I = np.array(ANH4I).mean()

				ANH4J = aconc_in.variables['ANH4J'][:,lay,row,col]
				ANH4J = np.array(ANH4J).mean()

				ANO3I = aconc_in.variables['ANO3I'][:,lay,row,col]
				ANO3I = np.array(ANO3I).mean()

				ANO3J = aconc_in.variables['ANO3J'][:,lay,row,col]
				ANO3J = np.array(ANO3J).mean()

				ASOIL = aconc_in.variables['ASOIL'][:,lay,row,col]
				ASOIL = np.array(ASOIL).mean()

				ASO4I = aconc_in.variables['ASO4I'][:,lay,row,col]
				ASO4I = np.array(ASO4I).mean()

				ASO4J = aconc_in.variables['ASO4J'][:,lay,row,col]
				ASO4J = np.array(ASO4J).mean()

				ALVPO1I = aconc_in.variables['ALVPO1I'][:,lay,row,col]
				ALVPO1I = np.array(ALVPO1I).mean()

				ASVPO1I = aconc_in.variables['ASVPO1I'][:,lay,row,col]
				ASVPO1I = np.array(ASVPO1I).mean()

				ASVPO2I = aconc_in.variables['ASVPO2I'][:,lay,row,col]
				ASVPO2I = np.array(ASVPO2I).mean()

				ALVOO1I = aconc_in.variables['ALVOO1I'][:,lay,row,col]
				ALVOO1I = np.array(ALVOO1I).mean()

				ALVOO2I = aconc_in.variables['ALVOO2I'][:,lay,row,col]
				ALVOO2I = np.array(ALVOO2I).mean()

				ASVOO1I = aconc_in.variables['ASVOO1I'][:,lay,row,col]
				ASVOO1I = np.array(ASVOO1I).mean()

				ASVOO2I = aconc_in.variables['ASVOO2I'][:,lay,row,col]
				ASVOO2I = np.array(ASVOO2I).mean()

				ALVPO1J = aconc_in.variables['ALVPO1J'][:,lay,row,col]
				ALVPO1J = np.array(ALVPO1J).mean()

				ASVPO1J = aconc_in.variables['ASVPO1J'][:,lay,row,col]
				ASVPO1J = np.array(ASVPO1J).mean()

				ASVPO2J = aconc_in.variables['ASVPO2J'][:,lay,row,col]
				ASVPO2J = np.array(ASVPO2J).mean()

				ASVPO3J = aconc_in.variables['ASVPO3J'][:,lay,row,col]
				ASVPO3J = np.array(ASVPO3J).mean()

				AIVPO1J = aconc_in.variables['AIVPO1J'][:,lay,row,col]
				AIVPO1J = np.array(AIVPO1J).mean()

				AXYL1J = aconc_in.variables['AXYL1J'][:,lay,row,col]
				AXYL1J = np.array(AXYL1J).mean()

				AXYL2J = aconc_in.variables['AXYL2J'][:,lay,row,col]
				AXYL2J = np.array(AXYL2J).mean()

				AXYL3J = aconc_in.variables['AXYL3J'][:,lay,row,col]
				AXYL3J = np.array(AXYL3J).mean()

				ATOL1J = aconc_in.variables['ATOL1J'][:,lay,row,col]
				ATOL1J = np.array(ATOL1J).mean()

				ATOL2J = aconc_in.variables['ATOL2J'][:,lay,row,col]
				ATOL2J = np.array(ATOL2J).mean()

				ATOL3J = aconc_in.variables['ATOL3J'][:,lay,row,col]
				ATOL3J = np.array(ATOL3J).mean()

				ABNZ1J = aconc_in.variables['ABNZ1J'][:,lay,row,col]
				ABNZ1J = np.array(ABNZ1J).mean()

				ABNZ2J = aconc_in.variables['ABNZ2J'][:,lay,row,col]
				ABNZ2J = np.array(ABNZ2J).mean()

				ABNZ3J = aconc_in.variables['ABNZ3J'][:,lay,row,col]
				ABNZ3J = np.array(ABNZ3J).mean()

				AISO1J = aconc_in.variables['AISO1J'][:,lay,row,col]
				AISO1J = np.array(AISO1J).mean()

				AISO2J = aconc_in.variables['AISO2J'][:,lay,row,col]
				AISO2J = np.array(AISO2J).mean()

				AISO3J = aconc_in.variables['AISO3J'][:,lay,row,col]
				AISO3J = np.array(AISO3J).mean()

				ATRP1J = aconc_in.variables['ATRP1J'][:,lay,row,col]
				ATRP1J = np.array(ATRP1J).mean()

				ATRP2J = aconc_in.variables['ATRP2J'][:,lay,row,col]
				ATRP2J = np.array(ATRP2J).mean()

				ASQTJ = aconc_in.variables['ASQTJ'][:,lay,row,col]
				ASQTJ = np.array(ASQTJ).mean()

				AALK1J = aconc_in.variables['AALK1J'][:,lay,row,col]
				AALK1J = np.array(AALK1J).mean()

				AALK2J = aconc_in.variables['AALK2J'][:,lay,row,col]
				AALK2J = np.array(AALK2J).mean()

				AORGCJ = aconc_in.variables['AORGCJ'][:,lay,row,col]
				AORGCJ = np.array(AORGCJ).mean()

				AOLGBJ = aconc_in.variables['AOLGBJ'][:,lay,row,col]
				AOLGBJ = np.array(AOLGBJ).mean()

				AOLGAJ = aconc_in.variables['AOLGAJ'][:,lay,row,col]
				AOLGAJ = np.array(AOLGAJ).mean()

				APAH1J = aconc_in.variables['APAH1J'][:,lay,row,col]
				APAH1J = np.array(APAH1J).mean()

				APAH2J = aconc_in.variables['APAH2J'][:,lay,row,col]
				APAH2J = np.array(APAH2J).mean()

				APAH3J = aconc_in.variables['APAH3J'][:,lay,row,col]
				APAH3J = np.array(APAH3J).mean()

				ALVOO1J = aconc_in.variables['ALVOO1J'][:,lay,row,col]
				ALVOO1J = np.array(ALVOO1J).mean()

				ALVOO2J = aconc_in.variables['ALVOO2J'][:,lay,row,col]
				ALVOO2J = np.array(ALVOO2J).mean()

				ASVOO1J = aconc_in.variables['ASVOO1J'][:,lay,row,col]
				ASVOO1J = np.array(ASVOO1J).mean()

				ASVOO2J = aconc_in.variables['ASVOO2J'][:,lay,row,col]
				ASVOO2J = np.array(ASVOO2J).mean()

				ASVOO3J = aconc_in.variables['ASVOO3J'][:,lay,row,col]
				ASVOO3J = np.array(ASVOO3J).mean()

				APCSOJ = aconc_in.variables['APCSOJ'][:,lay,row,col]
				APCSOJ = np.array(APCSOJ).mean()

				AALJ = aconc_in.variables['AALJ'][:,lay,row,col]
				AALJ = np.array(AALJ).mean()

				ASIJ = aconc_in.variables['ASIJ'][:,lay,row,col]
				ASIJ = np.array(ASIJ).mean()

				AFEJ = aconc_in.variables['AFEJ'][:,lay,row,col]
				AFEJ = np.array(AFEJ).mean()

				ATIJ = aconc_in.variables['ATIJ'][:,lay,row,col]
				ATIJ = np.array(ATIJ).mean()

				AOTHRI = aconc_in.variables['AOTHRI'][:,lay,row,col]
				AOTHRI = np.array(AOTHRI).mean()

				AOTHRJ = aconc_in.variables['AOTHRJ'][:,lay,row,col]
				AOTHRJ = np.array(AOTHRJ).mean()

				ACORS = aconc_in.variables['ACORS'][:,lay,row,col]
				ACORS = np.array(ACORS).mean()

				ASEACAT = aconc_in.variables['ASEACAT'][:,lay,row,col]
				ASEACAT = np.array(ASEACAT).mean()

				ASO4K = aconc_in.variables['ASO4K'][:,lay,row,col]
				ASO4K = np.array(ASO4K).mean()

				ANO3K = aconc_in.variables['ANO3K'][:,lay,row,col]
				ANO3K = np.array(ANO3K).mean()

				ANH4K = aconc_in.variables['ANH4K'][:,lay,row,col]
				ANH4K = np.array(ANH4K).mean()

				AMNJ = aconc_in.variables['AMNJ'][:,lay,row,col]
				AMNJ = np.array(AMNJ).mean()


				# species from pmdiag [3]
				PM25AT = pmdiag_in.variables['PM25AT'][:,lay,row,col]
				PM25AT = np.array(PM25AT).mean()

				PM25AC = pmdiag_in.variables['PM25AC'][:,lay,row,col]
				PM25AC = np.array(PM25AC).mean()

				PM25CO = pmdiag_in.variables['PM25CO'][:,lay,row,col]
				PM25CO = np.array(PM25CO).mean()

				 # species calculated inside SpecDef file [0]
				ANAK = 0.8373*ASEACAT + 0.0626*ASOIL + 0.0023*ACORS
				AMGK = 0.0997*ASEACAT + 0.0170*ASOIL + 0.0032*ACORS
				AKK = 0.0310*ASEACAT + 0.0242*ASOIL + 0.0176*ACORS
				ACAK = 0.0320*ASEACAT + 0.0838*ASOIL + 0.0562*ACORS

				APOCI = ALVPO1I /1.39 + ASVPO1I /1.32 + ASVPO2I /1.26
				ASOCI = ALVOO1I /2.27 + ALVOO2I /2.06 + ASVOO1I /1.88 + ASVOO2I /1.73
				APOCJ = ALVPO1J /1.39 + ASVPO1J /1.32 + ASVPO2J /1.26 +ASVPO3J /1.21 + AIVPO1J /1.17
				ASOCJ = AXYL1J /2.42  + AXYL2J /1.93  + AXYL3J /2.30 \
															 +ATOL1J /2.26  + ATOL2J /1.82  + ATOL3J /2.70 \
															 +ABNZ1J /2.68  + ABNZ2J /2.23  + ABNZ3J /3.00 \
															 +AISO1J /2.20  + AISO2J /2.23  + AISO3J /2.80 \
															 +ATRP1J /1.84  + ATRP2J /1.83  + ASQTJ /1.52  \
															 +AALK1J /1.56  + AALK2J /1.42                   \
															 +AORGCJ /2.00  + AOLGBJ /2.10  + AOLGAJ /2.50 \
															 +APAH1J /1.63  + APAH2J /1.49  + APAH3J /1.77 \
															 +ALVOO1J /2.27 + ALVOO2J /2.06 + ASVOO1J /1.88\
															 +ASVOO2J /1.73 + ASVOO3J /1.60 + APCSOJ  /2.00

				APOMI = ALVPO1I  + ASVPO1I  + ASVPO2I
				ASOMI = ALVOO1I  + ALVOO2I  + ASVOO1I  + ASVOO2I
				APOMJ = ALVPO1J  + ASVPO1J  + ASVPO2J  +ASVPO3J  + AIVPO1J
				ASOMJ = AXYL1J   + AXYL2J   + AXYL3J   + ATOL1J  \
															 +ATOL2J   + ATOL3J   + ABNZ1J   + ABNZ2J  \
														 +ABNZ3J   + AISO1J   + AISO2J   + AISO3J  \
														 +ATRP1J   + ATRP2J   + ASQTJ    + AALK1J  \
														 +AALK2J   + APAH1J   + APAH2J   + APAH3J  \
														 +AORGCJ   + AOLGBJ   + AOLGAJ               \
														 +ALVOO1J  + ALVOO2J  + ASVOO1J  + ASVOO2J \
														 +ASVOO3J  + APCSOJ
				AOCI = APOCI + ASOCI
				AOCJ = APOCJ + ASOCJ
				AOMI = APOMI    + ASOMI
				AOMJ = APOMJ    + ASOMJ
				ASOILJ = 2.20*AALJ + 2.49*ASIJ + 1.63*ACAJ + 2.42*AFEJ + 1.94*ATIJ
				ATOTI = ASO4I + ANO3I + ANH4I + ANAI + ACLI + AECI + AOMI + AOTHRI
				ATOTJ = ASO4J + ANO3J + ANH4J + ANAJ + ACLJ + AECJ + AOMJ + AOTHRJ + AFEJ + ASIJ + ATIJ + ACAJ + AMGJ + AMNJ + AALJ + AKJ
				ATOTK = ASOIL + ACORS + ASEACAT + ACLK + ASO4K + ANO3K + ANH4K

# !! PM2.5 species computed using modeled size distribution,
# reference: https://github.com/USEPA/CMAQ/blob/5.2/CCTM/src/MECHS/cb6r3_ae6_aq/SpecDef_cb6r3_ae6_aq.txt
				PM25_HP     = (AH3OPI * PM25AT + AH3OPJ * PM25AC + AH3OPK * PM25CO) * 1.0/19.0
				PM25_CL     = ACLI * PM25AT + ACLJ * PM25AC + ACLK * PM25CO
				PM25_EC     =    AECI * PM25AT + AECJ * PM25AC
				PM25_NA       =    ANAI * PM25AT + ANAJ * PM25AC + ANAK * PM25CO
				PM25_MG      = AMGJ * PM25AC + AMGK * PM25CO
				PM25_K       =     AKJ * PM25AC + AKK * PM25CO
				PM25_CA       =         ACAJ * PM25AC + ACAK * PM25CO
				PM25_NH4      =    ANH4I * PM25AT + ANH4J * PM25AC + ANH4K * PM25CO
				PM25_NO3    =    ANO3I * PM25AT + ANO3J * PM25AC + ANO3K * PM25CO
				PM25_OC      =   AOCI * PM25AT + AOCJ * PM25AC
				PM25_OM       =    AOMI * PM25AT + AOMJ * PM25AC
				PM25_SOIL       =    ASOILJ * PM25AC + ASOIL * PM25CO
				PM25_SO4       =    ASO4I * PM25AT + ASO4J * PM25AC + ASO4K * PM25CO
				PM25_TOT       =     ATOTI * PM25AT + ATOTJ * PM25AC + ATOTK * PM25CO
				PM25_UNSPEC1   =    PM25_TOT - (PM25_CL + PM25_EC + PM25_NA + PM25_NH4 + PM25_NO3 + PM25_OC + PM25_SOIL + PM25_SO4 )

				# now sum all species to get hourly PM2.5 concentratiosn
				daily_pm25_mean_cell_aconc = PM25_HP + PM25_CL + PM25_EC + PM25_NA + PM25_MG + PM25_K + PM25_CA + \
								PM25_NH4 + PM25_NO3 + PM25_OC + PM25_OM + PM25_SOIL + PM25_SO4 + PM25_TOT + PM25_UNSPEC1

				# fill the data-mesh with data, based on the order: z, x, y
				print( f'-> pin the data at day= {day_of_the_month-1} , row= {row} , col= {col}' )
				# add daily mean pm to each layer, row, col of pm25 mesh array
				pm25_mesh [ day_of_the_month-1 ][ row ][ col ] = daily_pm25_mean_cell_aconc
				# remove the 24-hr list for each row-col cell, it will be created for the next cell
				#del collected_24hr_pm_conc_list
		# close nc file
		aconc_in.close()
		pmdiag_in.close()
	# function returns the data-mesh to use in plotting
	return pm25_mesh

############### main ################

### file settings
cmaq_file_month = '10'
days_in_month = 1
Landis_scenario = '4'
#cmaq_pol = 'CO'
lay = 0
domain_cols = 250
domain_rows = 265

### get the starting time
print('-> start processing pm2.5...')
start = time.time()









# use the function
data_mesh = function_pm25_monthly_mean( days_in_month , domain_rows , domain_cols , lay )

print('-----------------------------')
print( f'-> number of dimensions= {data_mesh.ndim}' )
print( f'-> shape of data-mesh= {data_mesh.shape}' )

end = time.time()
print( f'-> time to complete the data_mesh: {end - start:.2f} sec' )  # f-string







