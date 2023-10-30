import arcpy
import os

# Set the workspace environment
arcpy.env.workspace = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_8_Creating_Geoprocessing_Tools_and_Sharing_Scripts\P8\P8\P8.gdb"

input_fc = arcpy.GetParameterAsText(0)
output_type = arcpy.GetParameterAsText(1)
output_folder = arcpy.GetParameterAsText(2)
file_name = arcpy.GetParameterAsText(3)

fc_path = os.path.join(arcpy.env.workspace, file_name)

arcpy.MakeFeatureLayer_management(input_fc, "fc_layer")

if output_type == "KMZ":
    out_kmz_file = "{}.KMZ".format(file_name)
    full_output_kmz_path = os.path.join(output_folder, out_kmz_file)
    arcpy.conversion.LayerToKML("fc_layer", full_output_kmz_path)
    arcpy.AddMessage("Exported successfully to KMZ")

elif output_type == "CAD":
    output_dwg_file = "{}.dwg".format(file_name)
    full_output_dwg_path = os.path.join(output_folder, output_dwg_file)
    arcpy.TableToCAD_conversion("fc_layer", full_output_dwg_path, "DWG_R2013")
    arcpy.AddMessage("Exported successfully to DWG")

arcpy.AddMessage("Process completed")
