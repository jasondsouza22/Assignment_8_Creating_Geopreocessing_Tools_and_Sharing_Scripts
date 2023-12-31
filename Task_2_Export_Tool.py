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
    output_CAD_file = "{}.dwg".format(file_name)
    full_output_CAD_path = os.path.join(output_folder,output_CAD_file)
    arcpy.conversion.ExportCAD(input_fc, "DWG_R2018", full_output_CAD_path)
    arcpy.AddMessage("Exported successfully to CAD")
arcpy.AddMessage("Process completed")
