from RFEM.initModel import Model, FirstFreeIdNumber
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.node import Node
from RFEM.enums import ObjectTypes


def line(node1: Node, node2: Node, comment: str = '', params: dict = None, model=Model):
    '''
    Args:
        node1 (Node): starting node
        node2 (Node) ending node
        comment (str, optional): Comments
        params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        model (RFEM Class, optional): Model to be edited
    '''

    return Line(FirstFreeIdNumber(ObjectTypes.E_OBJECT_TYPE_LINE),
                nodes_no=f"{node1.no} {node2.no}",
                comment=comment,
                params=params,
                model=model)
