from RFEM.TypesForMembers import memberHinge
from RFEM.initModel import Model, FirstFreeIdNumber
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.section import Section
from RFEM.enums import ObjectTypes
from RFEM.EzObjects.ezLine import line as ez_line


def member(start_section: Section, line: Line = None, node1: Node = None, node2: Node = None,
           end_section: Section = None, rotation_angle: float = 0.0, start_member_hinge: memberHinge = None,
           end_member_hinge: memberHinge = None, comment: str = '', params: dict = None, model=Model):
    """
    Args:
        start_section (Section): Start Section object
        line (Line, optional): Assigned Line
        node1 (Node, optional): Start Node
        node2 (Node, optional): End Node
        rotation_angle (float): Member Rotation Angle
        end_section (Section): Tag of End Section
        start_member_hinge_no (int): Tag of Start Member Hinge
        end_member_hinge_no (int): Tag of End Member Hinge
        comment (str, optional): Comment
        params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
        model (RFEM Class, optional): Model to be edited
    """

    if line is None:
        if node1 is None:
            raise ValueError(
                "Both line and node1 are None, either pass a line object, or two node objects to create a member")
        if node2 is None:
            raise ValueError(
                "Both line and node2 are None, either pass a line object, or two node objects to create a member")
        line = ez_line(node1=node1, node2=node2)
        node1_int = node1.no
        node2_int = node2.no
    else:
        node1_int = int(line.definition_nodes.split(' ')[0])
        node2_int = int(line.definition_nodes.split(' ')[1])

    return Member(no=FirstFreeIdNumber(ObjectTypes.E_OBJECT_TYPE_MEMBER),
                  start_node_no=node1_int,
                  end_node_no=node2_int,
                  rotation_angle=rotation_angle,
                  start_section_no=start_section.no if start_section else 0,
                  end_section_no=end_section.no if end_section else 0,
                  start_member_hinge_no=start_member_hinge.no if start_member_hinge else 0,
                  end_member_hinge_no=end_member_hinge.no if end_member_hinge else 0,
                  line=line,
                  comment=comment,
                  params=params,
                  model=model)