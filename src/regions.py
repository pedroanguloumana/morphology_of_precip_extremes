####################
# These regions are trimmed versions of the original regions as 
# defined at https://gpm.atmos.washington.edu/regions_v07.html
# They are trimmed as to remove overlap, so each region as defined here
# is disjoint from other regions. 
####################

GPM_REGIONS = {
    "AFC": {
        "long_name": "Africa",
        "lat_south": -40,
        "lat_north": 40,
        "lon_west": -30,  # trimmed to match with SAM region better
        "lon_east": 60,
    },
    "AKA": {
        "long_name": "Alaska",
        "lat_south": 35,
        "lat_north": 67,
        "lon_west": -178,
        "lon_east": -115,
    },
    "CIO": {
        "long_name": "Central Indian Ocean",
        "lat_south": -40,
        "lat_north": 10,
        "lon_west": 60,  # 55 originally, trimmed for AFC (60)
        "lon_east": 110,
    },
    "EPO": {
        "long_name": "Eastern Pacific Ocean",
        "lat_south": -67,
        "lat_north": 45,
        "lon_west": -178,
        "lon_east": -130,
    },
    "EUR": {
        "long_name": "Europe",
        "lat_south": 35,
        "lat_north": 67,
        "lon_west": -20,
        "lon_east": 45,
    },
    "H01": {
        "long_name": "Pacific West of South America (Hole1)",
        "lat_south": -67,
        "lat_north": 25,
        "lon_west": -130,  # -140 original, trimmed for EPO region (-130)
        "lon_east": -85,
    },
    "H02": {
        "long_name": "North Atlantic (Hole2)",
        "lat_south": 15,
        "lat_north": 67,
        "lon_west": -65,
        "lon_east": -10,
    },
    "H03": {
        "long_name": "South of Africa (Hole3)",
        "lat_south": -67,
        "lat_north": -35,
        "lon_west": -30,
        "lon_east": 75,
    },
    "H04": {
        "long_name": "South Indian Ocean (Hole4)",
        "lat_south": -67,
        "lat_north": -35,
        "lon_west": 70,
        "lon_east": 178,
    },
    "H05": {
        "long_name": "Western Pacific (Hole5)",
        "lat_south": 10,   # 5 originally, trimmed for WMP (10)
        "lat_north": 40,
        "lon_west": 130,   # 125 original, trimmed for SAS (130)
        "lon_east": 178,
    },
    "NAM": {
        "long_name": "North America",
        "lat_south": 15,
        "lat_north": 67,
        "lon_west": -140,
        "lon_east": -55,
    },
    "NAS": {
        "long_name": "North Asia",
        "lat_south": 35,
        "lat_north": 67,
        "lon_west": 40,
        "lon_east": 178,
    },
    "SAM": {
        "long_name": "South America",
        "lat_south": -67,
        "lat_north": 20,
        "lon_west": -85,  # -95 originally, trimmed for H01 (-85)
        "lon_east": -30,
    },
    "SAS": {
        "long_name": "South Asia",
        "lat_south": 10,  # 5 originally, trimmed for CIO (10)
        "lat_north": 40,
        "lon_west": 60,   # 55 original, trimmed for AFC (60)
        "lon_east": 130,
    },
    "WMP": {
        "long_name": "Warm Pool",
        "lat_south": -40,
        "lat_north": 10,
        "lon_west": 110,  # 105 original, trimmed for CIO (110)
        "lon_east": 178,
    },
}

def get_gpm_region_dict(region_key):
    r = GPM_REGIONS[region_key]
    return r

GSAM_REGIONS = {
    "EqIO": {
        "long_name": "Equatorial Indian Ocean",
        "lat_south": -10,
        "lat_north": 5,
        "lon_west": 60, 
        "lon_east": 90,
    },
    "AtlITCZ": {
        "long_name": "Atlantic ITCZ",
        "lat_south": -5,
        "lat_north": 5,
        "lon_west": -35,
        "lon_east": -10,
    },
    "PacITCZ": {
        "long_name": "Pacific ITCZ",
        "lat_south": -3,
        "lat_north": 7,
        "lon_west": -115,
        "lon_east": -85,
    }
}

def get_gsam_region_dict(region_key):
    r = GSAM_REGIONS[region_key]
    return r