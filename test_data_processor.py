import unittest
import data_processor
import numpy as np


class BaseTestCases(unittest.TestCase):

    # test for get_random_matrix
    def test_matrix(self):

        np.random.seed(6)

        self.assertEqual(data_processor.get_random_matrix(2, 3).shape, (2, 3))
        self.assertNotEqual(data_processor.get_random_matrix(2, 3).shape, (3, 3))

    # test for get_file_dimensions
    def test_file_dimensions(self):

        self.assertEqual(data_processor.get_file_dimensions("iris.data"), (149, 5))
        self.assertNotEqual(data_processor.get_file_dimensions("iris.data"), (149, 6))

    # test for write_matrix_to_file
    def test_write_matrix_to_file(self):

        np.random.seed(6)

        self.assertTrue(np.allclose(data_processor.write_matrix_to_file(4, 5,'np_iris.csv'),
            [
                [
                    0.07630828937395717,
                    0.7799187922401146,
                    0.4384092314408935,
                    0.7234651778309412,
                    0.9779895119966027,
                ],
                [
                    0.5384958704104337,
                    0.5011204636599379,
                    0.07205113335976154,
                    0.26843898010187117,
                    0.49988250082555996,
                ],
                [
                    0.6792299961209405,
                    0.8037390361043755,
                    0.3809411331485384,
                    0.06593634690590511,
                    0.28814559930799355,
                ],
                [
                    0.9095935277196137,
                    0.2133853535799155,
                    0.4521239618176831,
                    0.9312060196890217,
                    0.024899227550348013,
                ],
            ],
        ))


if __name__ == "__main__":
    unittest.main()
