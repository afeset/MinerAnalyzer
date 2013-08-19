#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import a.infra.misc.marker_file
import os

class SysVital(a.infra.misc.marker_file.ValidityMarker):
    def __init__ (self, logger, mountPoint):
        a.infra.misc.marker_file.ValidityMarker.__init__(self, logger, os.path.join(mountPoint, "vital.json"), instance="vital")

class SdVital(a.infra.misc.marker_file.ValidityMarker):
    def __init__ (self, logger, vitalPath):
        a.infra.misc.marker_file.ValidityMarker.__init__(self, logger, os.path.join(vitalPath, "sd-vital.json"), instance="sd-vital")

