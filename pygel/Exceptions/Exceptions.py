#
# Copyright (C) 2007 Saket Sathe
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#
# $LastChangedBy: xaeroman $
# $LastChangedDate: 2008-03-24 23:14:05 +0100 (Mon, 24 Mar 2008) $
# $LastChangedRevision: 88 $
# 
#


""" A module handling package exceptions

    @namespace PackageExceptions
"""

class Error(Exception):
    """ Empty base class from which all exceptions are derived

        \ingroup Exceptions
    """
    pass


class VertexError(Error):
    """ Represents a VertexError exception. It handles different types of graph vertex related exceptions

        \ingroup Exceptions
    """
 
    def __init__(self, vertexNumber, message):
        """ Contructs a VertexError exception

            @param vertexNumber Vertex number for which the exception occured
            @param message %Error message
        """
        ## Vertex number for which the exception occured
        self.vertexNumber = vertexNumber

        ## %Error message
        self.message = "VertexError: Vertex number = %s, Message = %s" % (vertexNumber,message)

class EdgeError(Error):
    """ Represents a EdgeError exception. It handles different types of graph edge related exceptions

        \ingroup Exceptions
       
    """
 
    def __init__(self, edgeNumber, message):
        """ Contructs a EdgeError exception

            @param edgeNumber Edge number for which the exception occured
            @param message %Error message
        """
        ## Vertex number for which the exception occured
        self.edgeNumber = edgeNumber

        ## %Error message
        self.message = "EdgeError: Edge number = %s, Message = %s" % (edgeNumber,message)


    def __init__(self, message):
        """ Contructs a EdgeError exception

            @param message %Error message
        """
        ## %Error message
        self.message = "EdgeError: Message = %s" % (message)

    def __init__(self, startVertexNumber, endVertexNumber, message):
        """ Contructs a EdgeError exception

            @param startVertexNumber startVertexNumber of the edge
            @param endVertexNumber endVertexNumber of the edge
            @param message %Error message
        """

        ## Start vertex number of the edge
        self.startVertexNumber = startVertexNumber

        ## End vertex number of the edge
        self.endVertexNumber = endVertexNumber
        
        ## %Error message
        self.message = "EdgeError: Start vertex number = %s, End vertex number = %s, Message = %s" % (str(startVertexNumber), str(endVertexNumber), message)

class DistError(Error):
    """ Represents a DistError exception. It handles different types of probability distribution related exceptions

        \ingroup Exceptions
    """
 
    def __init__(self, message):
        """ Contructs a DistError exception

            @param message %Error message
        """
        ## %Error message
        self.message = "DistError: Message = %s" % (message)

class ErrorMessages:
    """ Collection of various error message strings

        \ingroup Exceptions
    """
    vertexAlreadyExists = 'Vertex number already exists'
    vertexNotFound = 'Vertex number not found'
    edgeAlreadyExists = 'Edge already exists'
    edgeNotFound = 'Edge number not found'
    distAddOne = 'Probabilities do not add to one'
    noSelfLoops = 'No self loops are allowed for this graph'
