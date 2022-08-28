'''
configuration.py adds the parent directory of the NB_SEEA_ESRI repo in sys.path so that modules can be imported using "from NB_SEEA_ESRI..."
'''

import arcpy
import sys
import os

try:
    toolbox = "NB_SEEA_ESRI"

    currentPath = os.path.dirname(os.path.abspath(__file__)) # should go to <base path>\NB_SEEA_ESRI
    basePath = os.path.dirname(currentPath)

    nbSEEAPath = os.path.normpath(os.path.join(basePath, "NB_SEEA_ESRI"))

    libPath = os.path.join(nbSEEAPath, "lib")
    logPath = os.path.join(nbSEEAPath, "logs")
    tablesPath = os.path.join(nbSEEAPath, "tables")
    displayPath = os.path.join(nbSEEAPath, "display")
    mxdsPath = os.path.join(displayPath, "mxds")
    dataPath = os.path.join(nbSEEAPath, "data")
    stylesheetsPath = os.path.join(nbSEEAPath, "stylesheets")

    oldScratchPath = os.path.join(nbSEEAPath, "NBscratch")
    scratchPath = os.path.join(basePath, "NBscratch")

    userSettingsFile = os.path.join(nbSEEAPath, "user_settings.xml")
    filenamesFile = os.path.join(nbSEEAPath, "filenames.xml")
    labelsFile = os.path.join(nbSEEAPath, "labels.xml")

    # Add basePath to sys.path so that modules can be imported using "import NB_SEEA_ESRI.scripts.modulename" etc.
    if os.path.normpath(basePath) not in sys.path:
        sys.path.append(os.path.normpath(basePath))

    # Tolerance
    clippingTolerance = 0.00000000001

except Exception:
    arcpy.AddError("Configuration file not read successfully")
    raise
