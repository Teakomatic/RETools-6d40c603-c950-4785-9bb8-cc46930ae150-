"""
Line Smash Command

The command name is defined by the filname minus "_cmd.py"

"""

import rhinoscriptsyntax as rs

from __plugin__ import title, version

COMMAND_SUCCESS = 0; COMMAND_CANCEL = 1


def RunCommand( is_interactive ):
  
  print("Hello", title, version)
  
  # get a point
  point = rs.GetPoint()
  
  if point == None:
      return COMMAND_CANCEL
 
  rs.AddPoint(point)
  return COMMAND_SUCCESS