#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: effiz
# 

import xml.dom.minidom
def xmlToDict(xmlstring):
    """
    utility for converting xml to dictionary
    """
    doc = xml.dom.minidom.parseString(xmlstring)

    # remove empty nodes
    removeWhileSpaceNodes(doc.documentElement)
    dict_ = _elementToDict(doc.documentElement)
    return dict_

def _elementToDict(parent):
    # base case
    child = parent.firstChild
    if (not child):
        return None
    elif (child.nodeType == xml.dom.minidom.Node.TEXT_NODE):
        return child.nodeValue

    # recursive case
    d={}
    while child is not None:
        if (child.nodeType == xml.dom.minidom.Node.ELEMENT_NODE):
            elem = _elementToDict(child) # recursive step
            if isinstance(elem,dict): # a child with children of it's own
                if child.tagName not in d:
                    # first insertion of this type of node
                    d[child.tagName] = []
                d[child.tagName].append(elem)
            else:
                d[child.tagName] = elem # a leaf
        child = child.nextSibling
    return d

def removeWhileSpaceNodes(node, unlink=True):
    remove_list = []
    for child in node.childNodes:
        # if a node is empty of text - mark it for removal (remove after all children were handled)
        if child.nodeType == xml.dom.Node.TEXT_NODE and not child.data.strip():
            remove_list.append(child)
        elif child.hasChildNodes():
            # work the recursion down
            removeWhileSpaceNodes(child, unlink)

    # after children were handled - remove
    for node in remove_list:
        node.parentNode.removeChild(node)
        if unlink:
            node.unlink()
