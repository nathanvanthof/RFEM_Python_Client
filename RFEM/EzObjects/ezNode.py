from RFEM.initModel import Model, FirstFreeIdNumber
from RFEM.BasicObjects.node import Node
from RFEM.enums import ObjectTypes


def node(coordinate_X: float = 0.0, coordinate_Y: float = 0.0, coordinate_Z: float = 0.0, comment: str = '',
         params: dict = None, model=Model):
    '''
     Args:
        coordinate_X (float): X-Coordinate
        coordinate_Y (float): Y-Coordinate
        coordinate_Z (float): Z-Coordinate
        comment (str, optional): Comments
        params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        model (RFEM Class, optional): Model to be edited
    '''

    return Node(no=FirstFreeIdNumber(ObjectTypes.E_OBJECT_TYPE_NODE),
                coordinate_X=coordinate_X,
                coordinate_Y=coordinate_Y,
                coordinate_Z=coordinate_Z,
                comment=comment,
                params=params,
                model=model)
