from glob import glob
from src.regions import get_gpm_region_dict
import polars as pl
from src.globals import BASE_DIR

def load_global_merged_pf_stats():
    regions_list = ['AFC', 'CIO', 'EPO', 'H01', 'H05', 'SAM', 'SAS', 'WMP']
    scans = []
    for region in regions_list:
        region_dict = get_gpm_region_dict(region)
        f = BASE_DIR + f'data/gpm_precip_features/merged/merged.{region}.csv'
        scan = (
            pl.scan_csv(f)
            .filter(
                (pl.col("mean_latitude") < region_dict["lat_north"]) &
                (pl.col("mean_latitude") > region_dict["lat_south"]) &
                (pl.col("mean_longitude") < region_dict["lon_east"]) &
                (pl.col("mean_longitude") > region_dict["lon_west"]) &
                (pl.col("max_precip") >= 10) &
                (pl.col("is_complete")) &
                (pl.col("num_pixels") >= 10)
            )
            .with_columns([
                # parse e.g., "20150101_00:09:09" → Datetime
                pl.col("observation_time")
                  .cast(pl.Utf8)
                  .str.strptime(pl.Datetime, format="%Y%m%d_%H:%M:%S", strict=False)
                  .alias("observation_time"),
                pl.lit(region).alias("region"),
            ])
        )
        scans.append(scan)

    df_filtered = pl.concat(scans).collect(streaming=True)
    return df_filtered
