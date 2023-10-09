import teca
import numpy as np

class teca_heatwave_detect(teca.teca_python_algorithm):

    def __init__(self):
        self.verbose = False
        self.input_variable_name = 'VAR_2T'
        # set the default heatwave search location to Portland, OR
        self.heatwave_lat_location = 45.52
        self.heatwave_lon_location = -122.68 + 360
        self.heatwave_threshold = 273.15 + 32.0 # degrees K

    def set_heatwave_threshold(self, threshold : float):
        """ Set the heatwave threshold in degrees K. """
        self.heatwave_threshold = threshold

    def set_heatwave_location(self, lat : float, lon : float):
        """ Set the location for the heatwave search. """
        self.heatwave_lat_location = lat
        self.heatwave_lon_location = lon

    def set_input_variable_name(self, input_variable_name : str):
        """ Set the input variable name """
        self.input_variable_name = input_variable_name

    def set_verbose(self, verbose : bool = True):
        """ Set the verbose flag. When true the algorithm will print"""
        self.verbose = verbose

    def vprint(self, *args, **kwargs):
        """ Print if verbose is set """
        if self.verbose:
            print(*args, **kwargs)

    def request(self, port, md_in, req_in):
        """ Request one or more variables from upstream algorithms. """
        #self.vprint('teca_heatwave_detect::request')

        # copy the input metadata
        req = teca.teca_metadata(req_in)

        # set the input variable name
        req['arrays'] = self.input_variable_name

        # pass along the request
        return [req]

    def report(self, port, md_in):
        """ Report on array variable(s) this algorithm produces. """
        #self.vprint('teca_heatwave_detect::report')

        # copy the input metadata
        report_md = teca.teca_metadata(md_in[0])

        # this algorithm doesn't produce any arrays: only table entries. So just pass along the report
        return report_md

    def execute(self, port, data_in, req_in):
        """ Execute the algorithm. """
        #self.vprint('teca_heatwave_detect::execute')

        # get the input mesh
        in_mesh = teca.as_const_teca_cartesian_mesh(data_in[0])

        # get the lat/lon coordinates
        lat = np.array(in_mesh.get_y_coordinates())
        lon = np.array(in_mesh.get_x_coordinates())

        # get the number of lat/lon points
        nlat = len(lat)
        nlon = len(lon)

        # get the nearest lat/lon indices to the requested location
        lat_idx = np.argmin(np.abs(lat - self.heatwave_lat_location))
        lon_idx = np.argmin(np.abs(lon - self.heatwave_lon_location))

        # get the temperature variable
        arrays = in_mesh.get_point_arrays()
        t_var1d = arrays[self.input_variable_name].get_host_accessible()
        t_var = t_var1d.reshape([nlat, nlon])

        # extract the temperature at the requested location
        t_point = t_var[lat_idx, lon_idx]

        # determine if the temperature is at or above the threshold
        is_heatwave = False
        if t_point >= self.heatwave_threshold:
            is_heatwave = True
    
        # get the current time index
        index_request_key = req_in['index_request_key']
        index_request = req_in[index_request_key]
        t_index = index_request[0]
        # double check that only one index was requested
        if t_index != index_request[1]:
            raise NotImplementedError('teca_heatwave_detect::execute: only one time index can be requested at a time')

        # create the output table (necessary even if there is no heatwave)
        out_table = teca.teca_table.New()
        out_table.copy_metadata(in_mesh)

        # define the column
        out_table.declare_columns(['time_index'],['ul'])

        # add the time index to the table if it is a heatwave
        if is_heatwave:
            self.vprint('teca_heatwave_detect::execute: heatwave detected at time index ', t_index)
            out_table << t_index

        # return the current table row
        return out_table


