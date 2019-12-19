import os
from arcpy import Array
from arcpy import Describe
from arcpy import GetCellValue_management
from arcpy import Polyline
from arcpy import Polygon
from arcpy import Point
from arcpy import PointGeometry
from arcpy.da import UpdateCursor


def project_point(x, y, from_spatial_reference, to_spatial_reference):
    new_point = Point(x, y)
    new_point_geom = PointGeometry(new_point, from_spatial_reference)
    projected_point = new_point_geom.projectAs(to_spatial_reference).firstPoint
    new_x = projected_point.X
    new_y = projected_point.Y
    return (new_x, new_y)

def _get_z_value(coords, raster):
    coords_string = "{} {}".format(*coords)
    eval_cell_value = GetCellValue_management(raster, coords_string)
    try:
        cell_value = float(eval_cell_value.getOutput(0))
    except ValueError:
        return 0
    return round(cell_value, 1)

def _update_poly_z(geom, raster, z_factor=1):
    geom_sr = geom.spatialReference  
    desc_raster = Describe(raster)    
    raster_sr = desc_raster.spatialReference 
    array = Array()
    for part in geom: # TODO: account for multipart geometry
        for pnt in part:
            projected_coords = project_point(pnt.X, pnt.Y, geom_sr, raster_sr)
            new_z = round(_get_z_value(projected_coords, raster) * z_factor, 1)
            # new_z = round(pnt.Z * z_factor, 1)
            pnt.Z = new_z
            array.add(pnt)
    return array

def _update_point_z(geom, raster, z_factor=1):
    geom_sr = geom.spatialReference  
    desc_raster = Describe(raster)    
    raster_sr = desc_raster.spatialReference
    pnt = geom.firstPoint # TODO: account for multipart geometry
    projected_coords = project_point(pnt.X, pnt.Y, geom_sr, raster_sr)
    new_z = round(_get_z_value(projected_coords, raster) * z_factor, 1)
    pnt.Z = new_z                  
    return pnt

def update_feature_z(fc, raster, z_factor=1, sql=None):
    desc_fc = Describe(fc)
    fc_sr = desc_fc.spatialReference
    with UpdateCursor(fc, ["SHAPE@"], sql) as cursor:
        for row in cursor:
            geom = row[0]
            if geom.type == "polyline":
                array = _update_poly_z(geom, raster, z_factor)           
                new_geom = Polyline(array, fc_sr, True)
            elif geom.type == "polygon":
                array = _update_poly_z(geom, raster, z_factor)           
                new_geom = Polygon(array, fc_sr, True)
            elif geom.type == "point":
                new_geom = _update_point_z(geom, raster, z_factor)
            else:
                try:
                    raise ValueError('Function requires polyline, polygon, or point feature class')
                except ValueError as exc:
                    print(exc)
            cursor.updateRow([new_geom])

if __name__ == '__main__':
    fc = r"C:\Users\brbatt\Documents\!Noise\US98\GIS\DATA\barrier.shp"
    raster = r"C:\Users\brbatt\Documents\!Noise\US98\GIS\DATA\ned_existing_3m.tif"
    sql = """ name <> 'SIDEBAR' """
    update_feature_z(fc, raster, z_factor=3.2808399, sql=sql)
