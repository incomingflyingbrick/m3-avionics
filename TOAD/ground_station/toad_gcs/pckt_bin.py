"""Place position packets into bins depending on itow value
Gregory Brooks 2017"""

from .toad_packets import *
from math import floor
from . import coords

class Ref_point:
    def __init(self):
        self.e_coord = 0   # m
        self.n_coord = 0   # m
        self.u_coord = 0   # m
        self.distance = 0  # m

class Position_measurement:
    def __init__(self,itow_s):
        self.itow_s = itow_s  # GPS itow
        self.flags = 0
        self.full = False
        self.toads = []
        for count in range (0,NUM_TOADS):
            toad = Ref_point()
            self.toads.append(toad)  # List of toads, containing position and tof

    def set_dist(self,id,dist):
        self.toads[id].distance = dist
        # Set flags
        self.flags = self.flags | 2**(id)
        self.check_full()

    def set_pos(self,id,e,n,u):
        self.toads[id].e_coord = e
        self.toads[id].n_coord = n
        self.toads[id].u_coord = u

    def check_full(self):
        global last_known_e
        global last_known_n
        global last_known_u
        if self.flags == 2**NUM_TOADS - 1:
            self.full = True
            # Now populate ref point locations with last known position
            for count in range (0,NUM_TOADS):
                self.set_pos(count,last_known_e[count],last_known_n[count],last_known_u[count])

measurement_list = [] # newer bins -> higher index
MAX_BINS = 100  # Delete oldest unfilled bins once measurement_list gets too large
last_known_e = [0]*NUM_TOADS
last_known_n = [0]*NUM_TOADS
last_known_u = [0]*NUM_TOADS

def add_packet(packet):
    global measurement_list
    global MAX_BINS
    global last_known_e
    global last_known_n
    global last_known_u

    # If measurement_list is too large, delete oldest unfilled bin
    end = len(measurement_list)
    if end > MAX_BINS:
        del measurement_list[0:end-100]

    # Process new packet
    if packet.toad_id == TOAD_1:
        id = 0
    elif packet.toad_id == TOAD_2:
        id = 1
    elif packet.toad_id == TOAD_3:
        id = 2
    elif packet.toad_id == TOAD_4:
        id = 3
    elif packet.toad_id == TOAD_5:
        id = 4
    elif packet.toad_id == TOAD_6:
        id = 5

    if packet.log_type == MESSAGE_POSITION:
        # Update last known position
        enu_coords = coords.convert_llh_to_ENU([packet.lat,packet.lon,packet.height])
        last_known_e[id] = enu_coords[0]
        last_known_n[id] = enu_coords[1]
        last_known_u[id] = enu_coords[2]

    elif packet.log_type == MESSAGE_RANGING:
        itow_s = floor(packet.i_tow/1000)  # Second of the week the packet is timestamped with

        found_bin = MAX_BINS
        for index,bin in enumerate(measurement_list):
            if bin.itow_s == itow_s:
                # Place new packet into existing bin
                found_bin = index
                break
            else:
                # Need to create new bin
                found_bin = MAX_BINS  # i.e. not indexes 0 to NUM_TOADS-1

        if found_bin == MAX_BINS:
            # Create new bin
            new_bin = Position_measurement(itow_s)
            measurement_list.append(new_bin)
            found_bin = len(measurement_list) - 1

        # Put distance into found bin
        measurement_list[found_bin].set_dist(id,packet.dist())

        # Check for full bin to return
        for index,bin in enumerate(measurement_list):
            if bin.full:
                full_bin = index
                break
            else:
                full_bin = len(measurement_list)

        if full_bin != len(measurement_list):
            ## TODO: Log unfilled bins that are older than returned bin

            # Then delete the older bins
            rtrn_val = measurement_list[full_bin]
            del measurement_list[0:full_bin+1]
            return rtrn_val