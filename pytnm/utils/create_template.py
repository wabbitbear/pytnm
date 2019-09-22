import os
from arcpy import CreateFeatureclass_management as cf
from arcpy import AddField_management as af
from arcpy import env

# env.overwriteOutput = True
input_folder = r"C:\Users\brbatt\PyCharmProjects\pytnm\gis\DATA"

def create_receivers(input_folder):
    receivers = cf(out_path=input_folder,
        out_name="receiver",
        geometry_type="POINT",
        template=None,
        has_m="ENABLED",
        has_z="ENABLED",
        spatial_reference=None
    )
    af(in_table=receivers, 
        field_name="rec_id", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=10,
        field_alias="rec_id",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="x", 
        field_type="DOUBLE",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="x",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="y", 
        field_type="DOUBLE",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="y",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="z", 
        field_type="DOUBLE",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="z",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="du", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="du",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="bldg_hgt", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="bldg_hgt",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="land_use", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=100,
        field_alias="land_use",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="nac_cat", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=1,
        field_alias="nac_cat",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="nac_lvl", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="nac_lvl",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="ext_use", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=1,
        field_alias="ext_use",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="displace", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=1,
        field_alias="displace",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="bldg_row", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="bldg_row",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="ex_snd", 
        field_type="DOUBLE",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="ex_snd",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="nobld_snd", 
        field_type="DOUBLE",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="nobld_snd",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="bld_snd", 
        field_type="DOUBLE",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="bld_snd",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="ex_imp", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=10,
        field_alias="ex_imp",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="nobld_imp", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=10,
        field_alias="nobld_imp",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="bld_imp", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=10,
        field_alias="bld_imp",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )

def create_existing_roadway(input_folder):
    existing_roadways = cf(out_path=input_folder,
        out_name="existing_roadway",
        geometry_type="POLYLINE",
        template=None,
        has_m="ENABLED",
        has_z="ENABLED",
        spatial_reference=None
    )
    af(in_table=existing_roadways, 
        field_name="road_name", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=32,
        field_alias="road_name",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=existing_roadways, 
        field_name="exist_traf", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="exist_traf",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=existing_roadways, 
        field_name="nobld_traf", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="nobld_traf",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=existing_roadways, 
        field_name="div_lanes", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="div_lanes",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=existing_roadways, 
        field_name="speed", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="speed",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=existing_roadways, 
        field_name="ex_total", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="ex_total",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=existing_roadways, 
        field_name="nb_total", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="nb_total",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=existing_roadways, 
        field_name="med_pct", 
        field_type="FLOAT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="med_pct",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=existing_roadways, 
        field_name="hvy_pct", 
        field_type="FLOAT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="hvy_pct",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )

def create_proposed_roadway(input_folder):
    proposed_roadways = cf(out_path=input_folder,
        out_name="proposed_roadway",
        geometry_type="POLYLINE",
        template=None,
        has_m="ENABLED",
        has_z="ENABLED",
        spatial_reference=None
    )
    af(in_table=proposed_roadways, 
        field_name="road_name", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=32,
        field_alias="road_name",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=proposed_roadways, 
        field_name="bld_traf", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="bld_traf",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=proposed_roadways, 
        field_name="div_lanes", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="div_lanes",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=proposed_roadways, 
        field_name="speed", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="speed",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=proposed_roadways, 
        field_name="bld_total", 
        field_type="SHORT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="bld_total",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=proposed_roadways, 
        field_name="med_pct", 
        field_type="FLOAT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="med_pct",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=proposed_roadways, 
        field_name="hvy_pct", 
        field_type="FLOAT",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="hvy_pct",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )

def create_barrier(input_folder):
    barrier = cf(out_path=input_folder,
        out_name="barrier",
        geometry_type="POLYLINE",
        template=None,
        has_m="ENABLED",
        has_z="ENABLED",
        spatial_reference=None
    )
    af(in_table=barrier, 
        field_name="name", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=32,
        field_alias="name",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=barrier, 
        field_name="feasible", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=1,
        field_alias="feasible",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=barrier, 
        field_name="reasonable", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=1,
        field_alias="reasonable",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
def create_terrain_line(input_folder):
    terrain_line = cf(out_path=input_folder,
        out_name="terrain_line",
        geometry_type="POLYLINE",
        template=None,
        has_m="ENABLED",
        has_z="ENABLED",
        spatial_reference=None
    )
    af(in_table=terrain_line, 
        field_name="name", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=32,
        field_alias="name",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )

def create_study_area(input_folder):
    study_area = cf(out_path=input_folder,
        out_name="study_area",
        geometry_type="POLYGON",
        template=None,
        has_m="ENABLED",
        has_z="ENABLED",
        spatial_reference=None
    )
    af(in_table=study_area, 
        field_name="name", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=10,
        field_alias="name",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )

def create_study_receivers(input_folder):
    receivers = cf(out_path=input_folder,
        out_name="study_receiver",
        geometry_type="POINT",
        template=None,
        has_m="ENABLED",
        has_z="ENABLED",
        spatial_reference=None
    )
    af(in_table=receivers, 
        field_name="rec_id", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=10,
        field_alias="rec_id",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="x", 
        field_type="DOUBLE",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="x",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="y", 
        field_type="DOUBLE",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="y",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="z", 
        field_type="DOUBLE",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="z",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )

def create_field_measurements(input_folder):
    receivers = cf(out_path=input_folder,
        out_name="field_measurement",
        geometry_type="POINT",
        template=None,
        has_m="ENABLED",
        has_z="ENABLED",
        spatial_reference=None
    )
    af(in_table=receivers, 
        field_name="rec_id", 
        field_type="TEXT",
        field_precision=None,
        field_scale=None, 
        field_length=10,
        field_alias="rec_id",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="x", 
        field_type="DOUBLE",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="x",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="y", 
        field_type="DOUBLE",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="y",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )
    af(in_table=receivers, 
        field_name="z", 
        field_type="DOUBLE",
        field_precision=None,
        field_scale=None, 
        field_length=None,
        field_alias="z",
        field_is_nullable="NULLABLE",
        field_is_required="NON_REQUIRED",
        field_domain=None
    )

def main():
    create_receivers(input_folder)
    create_existing_roadway(input_folder)
    create_proposed_roadway(input_folder)
    create_barrier(input_folder)
    create_terrain_line(input_folder)
    create_study_area(input_folder)
    create_study_receivers(input_folder)
    create_field_measurements(input_folder)

if __name__ == '__main__':
    main()
