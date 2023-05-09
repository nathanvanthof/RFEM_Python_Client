from RFEM.initModel import Model, FirstFreeIdNumber
from RFEM.TypesForMembers import memberHinge
from RFEM.enums import ObjectTypes, MemberHingeNonlinearity
from RFEM.dataTypes import inf


def hinge(coordinate_system: str = "Local", member: str = "",
          translational_release_n: float = inf, translational_release_vy: float = inf, translational_release_vz: float = inf,
          rotational_release_mt: float = inf, rotational_release_my: float = 0.0, rotational_release_mz: float = 0.0,
          translational_release_n_nonlinearity=[MemberHingeNonlinearity.NONLINEARITY_TYPE_NONE],
          translational_release_vy_nonlinearity=[MemberHingeNonlinearity.NONLINEARITY_TYPE_NONE],
          translational_release_vz_nonlinearity=[MemberHingeNonlinearity.NONLINEARITY_TYPE_NONE],
          rotational_release_mt_nonlinearity=[MemberHingeNonlinearity.NONLINEARITY_TYPE_NONE],
          rotational_release_my_nonlinearity=[MemberHingeNonlinearity.NONLINEARITY_TYPE_NONE],
          rotational_release_mz_nonlinearity=[MemberHingeNonlinearity.NONLINEARITY_TYPE_NONE],
          comment: str = '', params: dict = None, model=Model):
    """
    Args:
        coordinate_system (str): Coordinate System Selection
        member (str): Assigned Members
        translational_release_n (float): Translational Spring Constant X
        translational_release_vy (float): Translational Spring Constant Y
        translational_release_vz (float): Translational Spring Constant Z
        rotational_release_mt (float): Rotational Spring Constant X
        rotational_release_my (float): Rotational Spring Constant Y
        rotational_release_mz (float): Rotational Spring Constant Z
        translational_release_n_nonlinearity (list): Nonlinearity Options Translational X
        translational_release_vy_nonlinearity (list): Nonlinearity Options Translational Y
        translational_release_vz_nonlinearity (list): Nonlinearity Options Translational Z
        rotational_release_mt_nonlinearity (list): Nonlinearity Options Rotational X
        rotational_release_my_nonlinearity (list): Nonlinearity Options Rotational Y
        rotational_release_mz_nonlinearity (list): Nonlinearity Options Rotational Z
        comment (str, optional): Comment
        params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        model (RFEM Class, optional): Model to be edited
    """

    return memberHinge(no=FirstFreeIdNumber(ObjectTypes.E_OBJECT_TYPE_MEMBER_HINGE),
                       member=member,
                       translational_release_n=translational_release_n,
                       translational_release_vy=translational_release_vy,
                       translational_release_vz=translational_release_vz,
                       rotational_release_mt=rotational_release_mt,
                       rotational_release_my=rotational_release_my,
                       rotational_release_mz=rotational_release_mz,
                       translational_release_n_nonlinearity=translational_release_n_nonlinearity,
                       translational_release_vy_nonlinearity=translational_release_vy_nonlinearity,
                       translational_release_vz_nonlinearity=translational_release_vz_nonlinearity,
                       rotational_release_mt_nonlinearity=rotational_release_mt_nonlinearity,
                       rotational_release_my_nonlinearity=rotational_release_my_nonlinearity,
                       rotational_release_mz_nonlinearity=rotational_release_mz_nonlinearity,
                       comment=comment,
                       params=params,
                       model=model)
