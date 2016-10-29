# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WikimapiaLayers
                                 A QGIS plugin
 This plugin extracts data from wikimapia and creates layers by each feature category
                             -------------------
        begin                : 2016-10-29
        copyright            : (C) 2016 by Alexander Ayoupov
        email                : ayoupov@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WikimapiaLayers class from file WikimapiaLayers.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .wm_layers import WikimapiaLayers
    return WikimapiaLayers(iface)
