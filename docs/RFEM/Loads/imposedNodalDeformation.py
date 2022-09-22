from RFEM.initModel import Model, clearAttributes

class ImposedNodalDeformation():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 node_no: str = '1',
                 load_parameter = None,
                 comment: str = '',
                 params: dict = {}):
        '''
        load_parameter:
            load_parameter = [imposed_displacement_x, imposed_displacement_y, imposed_displacement_z, imposed_rotation_x, imposed_rotation_y imposed_rotation_z]
        '''
        # Client model | Imposed Nodal Deformation
        clientObject = Model.clientModel.factory.create('ns0:imposed_nodal_deformation')

        # Clears object attributes | Sets all attributes to None
        clearAttributes(clientObject)

        # Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Assigned Node No.
        #clientObject.node_no = ConvertToDlString(node_no()
        clientObject.nodes = node_no

        # Load Parameter
        clientObject.imposed_displacement_x = load_parameter[0]
        clientObject.imposed_displacement_y = load_parameter[1]
        clientObject.imposed_displacement_z = load_parameter[2]

        clientObject.imposed_rotation_x = load_parameter[3]
        clientObject.imposed_rotation_y = load_parameter[4]
        clientObject.imposed_rotation_z = load_parameter[5]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Imposed Nodal Deformation to client model
        Model.clientModel.service.set_imposed_nodal_deformation(load_case_no, clientObject)
