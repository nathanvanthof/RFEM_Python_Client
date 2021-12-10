from RFEM.enums import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.modalAnalysisSettings import ModalAnalysisSettings
import sys
import pytest
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

def test_modal_analysis_implemented():

    exist = method_exists(clientModel,'set_modal_analysis_settings')
    assert exist == False #test fail once method is in T9 master or GM

@pytest.mark.skip("all tests still WIP")
def test_modal_analysis_settings():

    # modal analysis not yet implemmented in released RFEM6
    Model(True, "ModalAnalysis")
    Model.clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Crate Section
    Section(1, 'IPE 300', 1)

    # Create Nodes
    Node(1, 0, 0, 0)
    Node(2, 0, 0, -5)

    # Create Member
    Member(1, MemberType.TYPE_BEAM, 1, 2, 0, 1, 1)

    # Create Nodal Support
    NodalSupport(1, '1', NodalSupportType.FIXED)

    # Static Analysis Settings
    StaticAnalysisSettings(1, 'Geometrically Linear',
                           StaticAnalysisType.GEOMETRICALLY_LINEAR)

    # Modal Analysis Settings
    ModalAnalysisSettings(1, 'Modal Analysis Settings', ModalSolutionMethod.METHOD_LANCZOS, ModalMassConversionType.MASS_CONVERSION_TYPE_Z_COMPONENTS_OF_LOADS,
                          ModalMassMatrixType.MASS_MATRIX_TYPE_DIAGONAL, 2, [False, False, False, False, True, True])

    # Load Case Static
    # LoadCase(1, 'DEAD', [True, 0, 0, 1])
    modalParams = {
        "analysis_type": AnalysisType.ANALYSIS_TYPE_MODAL.name,
        "modal_analysis_settings":1,
    }
    # Load Case Modal
    LoadCase(2, 'MODAL',params=modalParams)
    Calculate_all()

    print('Ready!')

    Model.clientModel.service.finish_modification()

