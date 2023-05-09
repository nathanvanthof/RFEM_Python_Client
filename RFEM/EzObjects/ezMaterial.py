from RFEM.initModel import Model, FirstFreeIdNumber
from RFEM.BasicObjects.material import Material
from RFEM.enums import ObjectTypes


def material(name: str, comment: str = '', params: dict = None, model = Model):
    """
            name (str): Name of Desired Material (As Named in RFEM Database)
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
    """

    return Material(no=FirstFreeIdNumber(ObjectTypes.E_OBJECT_TYPE_MATERIAL),
                    name=name,
                    comment=comment,
                    params=params,
                    model=model)