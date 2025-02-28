"""
(*)~---------------------------------------------------------------------------
Pupil - eye tracking platform
Copyright (C) 2012-2019 Pupil Labs

Distributed under the terms of the GNU
Lesser General Public License (LGPL v3.0).
See COPYING and COPYING.LESSER for license details.
---------------------------------------------------------------------------~(*)
"""
import pytest

import numpy as np
import cv2


def test_solve_npn():

    camera_calibration  = {'dist_coefs': np.array([[-0.63037088,  0.17767048, -0.00489945, -0.00192122,  0.1757496 ]]) * 0, 'camera_name': 'Pupil Cam1 ID2', 'resolution': (1280, 720), 'camera_matrix': np.array([[  1200,   0.00000000e+00,   1280/2.],
       [  0.00000000e+00,   1200,   720/2.],
       [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00]])}

    camera_matrix = camera_calibration['camera_matrix']
    dist_coefs = camera_calibration['dist_coefs']

    image_points = np.array([
        [ 0, 0 ],
        [ 1280 , 720 ],
        [ 640 , 360 ],
        [ 0 , 720 ],
        [ 1280 , 0]
    ], dtype = np.float64)
    image_points.shape = (-1 , 1, 2)

    # TODO: Replace print with an assert for an expected property
    print(image_points.shape)

    object_points = np.array([
        [-640 , -360 , 1200],
        [640 , 360 , 1200],
        [0 , 0 , 1200],
        [-640 , 360 , 1200],
        [640 , -360 , 1200]
    ], dtype = np.float64)
    object_points *= 1,1,-1.

    # TODO: Replace print with an assert for an expected property
    print(object_points)

    # object_points += (30.,0.,400.)
    # TODO: Replace print with an assert for an expected property
    print(object_points.shape)

    object_points  = object_points.reshape(-1,3)
    result = cv2.solvePnP( object_points , image_points, camera_matrix, dist_coefs, flags=cv2.SOLVEPNP_ITERATIVE)

    # TODO: Replace print with an assert for an expected property
    print(result)

    rvec =   result[1]
    tvec =  result[2]

    gaze_point = [ 0 , 0 , 120 ]
    gaze_point = [ 0 , 0 , 1200 ]

    image_point, _  =  cv2.projectPoints( np.array([gaze_point] , dtype= np.float64) , rvec, tvec , camera_matrix , dist_coefs )

    # TODO: Replace print with an assert for an expected property
    print(image_point)

    # TODO: Replace print with an assert for an expected property
    print(np.linalg.norm(np.array(  [-155.9135437,    51.7420845,  -612.71209717]) - np.array( [-417.86495972 , -19.15872192 ,-465.78265381])))
