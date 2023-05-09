from RFEM.initModel import Model, FirstFreeIdNumber
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.enums import ObjectTypes


def section(name: str, material: Material, comment: str = '', params: dict = None, model=Model):
    """
    This method generates a section with the first free ID number

    Args:
            name: the section name (eg: "HEA 600")
            material: a Material object
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
    """

    return Section(no=FirstFreeIdNumber(ObjectTypes.E_OBJECT_TYPE_SECTION),
                   name=name,
                   material_no=material.no,
                   comment=comment,
                   params=params,
                   model=model)
