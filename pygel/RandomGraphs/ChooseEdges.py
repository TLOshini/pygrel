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
# $LastChangedDate: 2008-12-13 02:02:58 +0100 (Sat, 13 Dec 2008) $
# $LastChangedRevision: 96 $
# 
#

import threading, random


class ChooseEdges(threading.Thread):
    """ Thread for selecting a set of edges

        \ingroup RandomGraphs

    """
    ## Common serial edge list. Updated by each thread in a semaphoric operation
    serialEdgeList = []

    ## Lock that a thread acquires for performing a semaphoric operation
    lck = threading.Lock()
    evnt = threading.Event()

    ## Thread ID
    id = 0

    def __init__(self, noOfEdges, noSelfLoops, startVertX, endVertX, startVertY, endVertY, probA, probB, probC, probD):
        """ Constructs a selector thread

            @see RandomGraphs::DirectedPowerLawRandomGraph
        """

        threading.Thread.__init__(self)
        ## @see RandomGraphs::DirectedPowerLawRandomGraph
        self.startVertX = startVertX

        ## @see RandomGraphs::DirectedPowerLawRandomGraph
        self.endVertX = endVertX

        ## @see RandomGraphs::DirectedPowerLawRandomGraph
        self.startVertY = startVertY

        ## @see RandomGraphs::DirectedPowerLawRandomGraph
        self.endVertY = endVertY

        ## @see RandomGraphs::DirectedPowerLawRandomGraph
        self.noOfEdges = noOfEdges

        ## @see RandomGraphs::DirectedPowerLawRandomGraph
        self.probA = probA

        ## @see RandomGraphs::DirectedPowerLawRandomGraph
        self.probB = probB

        ## @see RandomGraphs::DirectedPowerLawRandomGraph
        self.probC = probC

        ## @see RandomGraphs::DirectedPowerLawRandomGraph
        self.probD = probD
        
        self.debug = 0
        
        ## @see RandomGraphs::DirectedPowerLawRandomGraph
        self.noSelfLoops = noSelfLoops

        ChooseEdges.id += 1

        ## Thread ID
        self.id = ChooseEdges.id
        

    def selectVertex(self, sVertX, eVertX, sVertY, eVertY, cumulativeA, cumulativeB, cumulativeC):
        """ Selects start and end vertices recursively

            @param sVertX Starting column of the adjacency matrix
            @param eVertX Ending column of the adjacency matrix
            @param sVertY Starting row of the adjacency matrix
            @param eVertY Ending column of the adjacency matrix
            @param cumulativeA Cumulative distribution 
            @param cumulativeB Cumulative distribution 
            @param cumulativeC Cumulative distribution 
            @return Selected vertices
        """

# Commented for future use:
#
#         #print "sVertX = %s, eVertX = %s, sVertY = %s, eVertY = %s" % (sVertX, eVertX, sVertY, eVertY)
#         if sVertX == eVertX and sVertY == eVertY:    
#             #if self.debug: print "sVertX = %s, eVertX = %s, sVertY = %s, eVertY = %s" % (sVertX, eVertX, sVertY, eVertY)
#             return [sVertX, eVertX, sVertY, eVertY]
    
        if abs(sVertX - eVertX) <= 1 and abs(sVertY - eVertY) <= 1:
            #if self.debug: print "sVertX = %s, eVertX = %s, sVertY = %s, eVertY = %s" % (sVertX, eVertX, sVertY, eVertY)
            return [sVertX, eVertX, sVertY, eVertY]

        selectedQuadrant = random.randint(0,3)

        initialSeed = random.uniform(0,1)

        if initialSeed >= 0 and initialSeed < cumulativeA:
            selectedQuadrant = 0

        elif initialSeed >= cumulativeA and initialSeed < cumulativeB:
            selectedQuadrant = 1

        elif initialSeed >= cumulativeB and initialSeed < cumulativeC:
            selectedQuadrant = 2

        elif initialSeed >= cumulativeC and initialSeed <= 1:
            selectedQuadrant = 3

        # print "quadrant selected = %s" % (selectedQuadrant)

        midPointX = (eVertX-sVertX)/2
        midPointY = (eVertY-sVertY)/2
        if selectedQuadrant == 0:
            sVertX = sVertX
            eVertX = eVertX - midPointX

            sVertY = sVertY
            eVertY = eVertY - midPointY

        if selectedQuadrant == 1:
            sVertX = sVertX + midPointX
            eVertX = eVertX

            sVertY = sVertY
            eVertY = eVertY - midPointY

        if selectedQuadrant == 2:
            sVertX = sVertX 
            eVertX = eVertX - midPointX
            
            sVertY = sVertY + midPointY
            eVertY = eVertY 

        if selectedQuadrant == 3:
            sVertX = sVertX + midPointX
            eVertX = eVertX
            
            sVertY = sVertY + midPointY
            eVertY = eVertY        

        return self.selectVertex(sVertX, eVertX, sVertY, eVertY, cumulativeA, cumulativeB, cumulativeC)

    
    def run(self):
        """ Start the thread
        """
        threadEdgeList = []

        step = int(0.05*self.noOfEdges)
        if step == 0:
            progressBar = xrange(0,self.noOfEdges,1)
        else:
            progressBar = xrange(0,self.noOfEdges,int(0.05*self.noOfEdges))

        noOfEdges = self.noOfEdges
        
        startVertX = self.startVertX
        endVertX = self.endVertX
        startVertY = self.startVertY
        endVertY = self.endVertY
        id = self.id
        selectVertex = self.selectVertex

        cumulativeA = self.probA
        cumulativeB = cumulativeA + self.probB
        cumulativeC = cumulativeB + self.probC
        
        threadEdgeListAppend = threadEdgeList.append
        
        for i in xrange(0,noOfEdges):

#            if i in progressBar:
#               print "Thread id %s, |--> %s edges added<--|" % (id, i)

            a = selectVertex(startVertX, endVertX, startVertY, endVertY, cumulativeA, cumulativeB, cumulativeC)
            startVertexNumber = min(a[0:1])
            endVertexNumber = min(a[2:3])
            
            if self.noSelfLoops == 0: 
                threadEdgeListAppend(startVertexNumber)
                threadEdgeListAppend(endVertexNumber)
            elif startVertexNumber != endVertexNumber:
                threadEdgeListAppend(startVertexNumber)
                threadEdgeListAppend(endVertexNumber)
            
        ChooseEdges.lck.acquire()
        ChooseEdges.serialEdgeList.extend(threadEdgeList)
        ChooseEdges.lck.release()

