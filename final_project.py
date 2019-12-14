#This script will automate the task of extracting bands from a multiband image
#once extracted the script will calculate indicies from NIR and RED bands including
#NDVI, SAVI, and EVI
#The script will then clip and reproject (optional) to a desired ROI

import arcpy
from arcpy.sa import *

arcpy.CheckInExtension("Spatial")
arcpy.CheckOutExtension("Spatial")

arcpy.env.overwriteOutput = True

#assign an image to the make raster layer tool.
#in order -> (composite geodataset, raster layer, SQL expression, Extent, Value Table).
#create NIR_1 band Variables
in_raster1 = Raster(arcpy.GetParameterAsText(0))
out_rasterlayer1 = Raster(arcpy.GetParameterAsText(1))
where_clause1 = (arcpy.GetParameterAsText(2))
envelope1 =(arcpy.GetParameterAsText(3))
band_index1 = (arcpy.GetParameterAsText(4))

#create raster layer NIR_1 band with make raster layer tool
NIR_1 = arcpy.MakeRasterLayer_management(in_raster1, out_rasterlayer1, {where_clause1}, {envelope1}, {band_index1})

#save NIR_1
NIR_1.save(arcpy.GetParameterAsText(5))

#create Red_1 variables
in_raster2 = Raster(arcpy.GetParameterAsText(6))
out_rasterlayer2 = Raster(arcpy.GetParameterAsText(7))
where_clause2 = (arcpy.GetParameterAsText(8))
envelope2 = (arcpy.GetParameterAsText(9))
band_index2 = (arcpy.GetParameterAsText(10))

#create raster layer Red_1 band with marke raster layer tool
Red_1 = arcpy.MakeRasterLayer_management (in_raster2, out_rasterlayer2, {where_clause2}, {envelope2}, {band_index2})

#save Red_1 
Red_1.save(arcpy.GetParameterAsText(11))

#create NIR_2 band Variables
in_raster3 = Raster(arcpy.GetParameterAsText(12))
out_rasterlayer3 = Raster(arcpy.GetParameterAsText(13))
where_clause3 = (arcpy.GetParameterAsText(14))
envelope3 =(arcpy.GetParameterAsText(15))
band_index3 = (arcpy.GetParameterAsText(16))

#create raster layer NIR_2 band with make raster layer tool
NIR_2 = arcpy.MakeRasterLayer_management(in_raster3, out_rasterlayer3, {where_clause3}, {envelope3}, {band_index3})

#save NIR_2
NIR_2.save(arcpy.GetParameterAsText(17))

#create Red_2 variables
in_raster4 = Raster(arcpy.GetParameterAsText(18))
out_rasterlayer4 = Raster(arcpy.GetParameterAsText(19))
where_clause4 = (arcpy.GetParameterAsText(20))
envelope4 = (arcpy.GetParameterAsText(21))
band_index4 = (arcpy.GetParameterAsText(22))

#create raster layer Red_1 band with marke raster layer tool
Red_2 = arcpy.MakeRasterLayer_management (in_raster4, out_rasterlayer4, {where_clause4}, {envelope4}, {band_index4})

#save Red_1 
Red_2.save(arcpy.GetParameterAsText(23))

Calculate NDVI
NDVI_1 = ((NIR_1 - Red1)/(NIR_1 + Red_1))
NDVI_1.save(arcpy.GetParameterAsText(24))

NDVI_2 = ((NIR_2 - Red_2)/(NIR_2 + Red_2))
NDVI_2.save(arcpy.GetParameterAsText(25))





