from PIL import Image
import numpy as np
import cmath

def checkIfDuplicates(listOfElems):
    """
    Check if given list contains any duplicates
    """
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)         
    return False

def makeOutputCanvas(width_resolution = 1000, height_resolution = 1000, depth = "", dtype = float, round = 6): #or dtype complex
    """
    Returns an empty np array of the correct depth for a gresycale or rgb image.
    """
    return np.zeros((width_resolution, height_resolution), dtype) if depth == 'greyscale' else np.zeros((width_resolution, height_resolution, 3), dtype)

def makeInputCanvas(width_resolution, height_resolution, width_offset, height_offset, width, height, dtype = float, round = 6): #or dtype complex
    """
    Returns an np array where each element (pixel) is its coordeinate scaled to fit.
    """
    returnArray = np.zeros((width_resolution, height_resolution), dtype) if dtype == complex else np.zeros((width_resolution, height_resolution, 2), dtype)
    
    if dtype == float:
        for width_coord in range(width_resolution):
            for height_coord in range(height_resolution):
                returnArray[width_coord, height_coord] = [width_coord/width_resolution*width + width_offset, height_coord/height_resolution*height + height_offset]
    
    if dtype == complex:
        for width_coord in range(width_resolution):
            for height_coord in range(height_resolution):
                returnArray[width_coord, height_coord] = complex(width_coord/width_resolution*width + width_offset, height_coord/height_resolution*height + height_offset)
    
    return returnArray
    
def checkBehavior(history):
    """
    Returns details about the behavior of a list. Either -1 for strictly decreasing, 
    0 for unchanging, +1 for strictly increasing, or +N for a number of periods.
    """
    #### SET UP BEHAVIOR 
    behavior = int(history[1] != history[0]) * (-1 if np.abs(history[1]) < np.abs(history[0]) else 1)
    strictDirection = True

    #### CHECK STRICT DIRECTION
    for index, val in enumerate(history):
        if index == 0: continue
        else: newBehavior = int(history[index] != history[index - 1]) * (-1 if np.abs(history[1]) < np.abs(history[0]) else 1)
        
        if newBehavior != behavior: behavior = 100; break #If behavior changes, it's erratic and is tested in another way.

    #### CHECK PERIODICITY
    #TODO
    #TODO
    #TODO
    
    #### RETURN FINDINGS
    return behavior

def checkEscape(number, function, iterations, funcArgs = None):
    """
    Input in the form applyFunc(number, function, iterations, [(funcArgs1, funcArgs2, ...)])

    Applies "function" to seed "number" for a set number of "iterations," then returns statistics 
    in the form (finalVal, history, behavior). Behavior is either -1 for strictly decreasing, 
    0 for unchanging, +1 for strictly increasing, or +N for a number of periods.
    """
    #### SET UP STATS
    history = []
    history.append(number)
    
    #### APPLY FUNCTION
    for iteration in range(iterations):
        number = function(number) if funcArgs is None else function(number, funcArgs)
        history.append(number)

    #### ANALYZE BEHAVIOR
    behavior = checkBehavior(history)

    #### RETURN FINDINGS
    return {"finalNumber":number, "history":history, "behavior":behavior}