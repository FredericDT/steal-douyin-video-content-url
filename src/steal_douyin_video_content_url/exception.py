class RenderDataObjectStrategyNotDefinedException(Exception):
    """Exception raised when all strategy failed to extract renderDataObject.
    """    
    pass

class RenderDataTagNotFoundException(Exception):
    """Exception raised when the given url does not contain a 'RENDER_DATA' tag.
    """
    pass

