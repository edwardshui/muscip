import unittest
import connectome
import fibers
import nibabel

fib = fibers.read('test_data/fibers/CMTK_scale33.trk')
roi = nibabel.load('test_data/images/CMTK_roi.nii.gz')
node_info = 'test_data/connectome/freesurfer_node_info.graphml'

class Test_TNConnectome(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_generate_connectome_from_fibers_and_rois(self):
        assert connectome.generate_connectome(fib, roi) is not None
    
    def test_node_info(self):
        my_connectome = connectome.generate_connectome(fib, roi, node_info=node_info)
        assert my_connectome.node[82]['name'] == 'Left-Amygdala'
        assert my_connectome.node[82]['region'] == 'subcortical'
        assert my_connectome.node[82]['hemisphere'] == 'left'

    def test_can_set_clinical_info(self):
        test_info = dict( group='foo',
                          gender='F',
                          a_score=114.56,
                          b_score=5 )
        my_connectome = connectome.generate_connectome(fib, roi)
        my_connectome.set_info(test_info)
        assert my_connectome.get_info() == test_info

    def test_can_read_gpickle(self):
        pass