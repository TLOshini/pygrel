#!/usr/bin/python
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
# $LastChangedDate: 2007-07-31 17:42:11 +0200 (Tue, 31 Jul 2007) $
# $LastChangedRevision: 56 $
#
#



from pygel.MetaClass.AbstractMethod import *
from pygel.MetaClass.MetaClass import *

class AbstractEdge:
    """ Abstract class for representing an edge

        \ingroup BaseElements
    """

    __metaclass__ = MetaClass

    ## Abstract method for obtaining the start vertex of an edge. 
    getStartVertex = AbstractMethod('getStartVertex')

    ## Abstract method for obtaining the end vertex of an edge. 
    getEndVertex = AbstractMethod('getEndVertex')

    ## Abstract method for setting the start vertex of an edge. 
    setStartVertex = AbstractMethod('getStartVertex')	

    ## Abstract method for setting the end vertex of an edge. 
    setEndVertex = AbstractMethod('getEndVertex')
