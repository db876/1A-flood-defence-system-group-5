# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa

def stations_within_radius(stations, centre, r):
    '''Required for task 1C - returns list of stations inside radius'''
    found_stations = []
    all_stations = stations_by_distance(stations, centre)
    for i in range(len(all_stations)):
        if all_stations[i](1) <= r:
            found_stations.append(all_stations[i](0))