import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_8_Creating_Geopreocessing_Tools_and_Sharing_Scripts\P8\P8\P8.gdb"


#Inputs
x_cord = arcpy.GetParameterAsText(0)
y_cord = arcpy.GetParameterAsText(1)
Output_fc_name = arcpy.GetParameterAsText(2)

fc_path = os.path.join(gdb_path, Output_fc_name)
# Point Object
pnt_obj = arcpy.Point(x_cord, y_cord)

# Spatial reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")

# Point Geometry
pnt_geom = arcpy.PointGeometry(pnt_obj, spatial_ref)

arcpy.CopyFeatures_management(pnt_geom, fc_path)

print("Process Completed")
