import unittest
from Domain.MyVector import MyVector
from Infrastructure.VectorRepository import VectorRepository
from Application.VectorController import VectorRepositoryController

class TestVectorOperations(unittest.TestCase):
    #testing the repository with the help of the controller
    def setUp(self):
        self.vector_repo = VectorRepository([])
        self.vector_controller = VectorRepositoryController(self.vector_repo)

    def test_add_vector(self):
        vector = MyVector(1, 'r', 1, [1, 2, 3])
        self.vector_controller.add_vector_repo(vector)
        self.assertEqual(len(self.vector_controller.get_vectors_repo()), 1)
        self.assertEqual(self.vector_controller.get_vectors_repo()[0].get_name_id(), 1)
        self.assertEqual(self.vector_controller.get_vectors_repo()[0].get_values(), [1, 2, 3])

    def test_get_all_vectors(self):
        vector1 = MyVector(1, 'r', 1, [1, 2])
        vector2 = MyVector(2, 'g', 1, [3, 4])
        self.vector_controller.add_vector_repo(vector1)
        self.vector_controller.add_vector_repo(vector2)
        vectors = self.vector_controller.get_vectors_repo()
        self.assertEqual(len(vectors), 2)
        self.assertEqual(vectors[0].get_name_id(), 1)
        self.assertEqual(vectors[1].get_name_id(), 2)

    def test_get_vector_at_index(self):
        vector = MyVector(3, 'b', 1, [1, 2, 3])
        self.vector_controller.add_vector_repo(vector)
        retrieved_vector = self.vector_controller.get_vector_at_index_repo(0)
        self.assertEqual(retrieved_vector.get_name_id(), 3)
        self.assertEqual(retrieved_vector.get_colour(), 'b')
        self.assertEqual(retrieved_vector.get_values(), [1, 2, 3])

    def test_update_vector_at_index(self):
        vector = MyVector(4, 'y', 1, [5, 6])
        self.vector_controller.add_vector_repo(vector)
        new_vector = MyVector(5, 'm', 1, [7, 8])
        self.vector_controller.update_vector_at_index_repo(0, new_vector)
        updated_vector = self.vector_controller.get_vector_at_index_repo(0)
        self.assertEqual(updated_vector.get_name_id(), 5)
        self.assertEqual(updated_vector.get_colour(), 'm')
        self.assertEqual(updated_vector.get_values(), [7, 8])

    def test_delete_vector_by_index(self):
        vector = MyVector(6, 'g', 1, [9, 10])
        self.vector_controller.add_vector_repo(vector)
        self.vector_controller.delete_vector_at_index_repo(0)
        self.assertEqual(len(self.vector_controller.get_vectors_repo()), 0)

    def test_delete_vector_by_nameID(self):
        vector1 = MyVector(7, 'r', 1, [1])
        vector2 = MyVector(8, 'g', 1, [2])
        self.vector_controller.add_vector_repo(vector1)
        self.vector_controller.add_vector_repo(vector2)
        self.vector_controller.delete_vector_by_nameID_repo(7)
        self.assertEqual(len(self.vector_controller.get_vectors_repo()), 1)
        self.assertEqual(self.vector_controller.get_vectors_repo()[0].get_name_id(), 8)

    def test_update_all_vectors_by_adding_scalar(self):
        vector1 = MyVector(9, 'g', 1, [1, 2])
        vector2 = MyVector(10, 'b', 1, [3, 4])
        self.vector_controller.add_vector_repo(vector1)
        self.vector_controller.add_vector_repo(vector2)
        self.vector_controller.update_by_adding_scalar_repo(1)
        self.assertEqual(self.vector_controller.get_vectors_repo()[0].get_values(), [2, 3])
        self.assertEqual(self.vector_controller.get_vectors_repo()[1].get_values(), [4, 5])

    def test_delete_vectors_between_indexes(self):
        vector1 = MyVector(11, 'y', 1, [1])
        vector2 = MyVector(12, 'g', 1, [2])
        vector3 = MyVector(13, 'r', 1, [3])
        self.vector_controller.add_vector_repo(vector1)
        self.vector_controller.add_vector_repo(vector2)
        self.vector_controller.add_vector_repo(vector3)
        self.vector_controller.delete_vectors_between_two_indexes_repo(0, 1)
        self.assertEqual(len(self.vector_controller.get_vectors_repo()), 1)
        self.assertEqual(self.vector_controller.get_vectors_repo()[0].get_name_id(), 13)

    def test_vectors_with_given_sum(self):
        vector1 = MyVector(14, 'g', 1, [1, 2])
        vector2 = MyVector(15, 'b', 1, [3, 3])
        self.vector_controller.add_vector_repo(vector1)
        self.vector_controller.add_vector_repo(vector2)
        result_vectors = self.vector_controller.vector_with_given_sum_repo(3)
        self.assertEqual(len(result_vectors), 1)
        self.assertEqual(result_vectors[0].get_name_id(), 14)
        self.assertEqual(result_vectors[0].sum_of_elements(), 3)

    def test_update_all_vectors_by_adding_scalar(self):
        vector1 = MyVector(9, 'g', 1, [1, 2])
        vector2 = MyVector(10, 'b', 1, [3, 4])
        self.vector_controller.add_vector_repo(vector1)
        self.vector_controller.add_vector_repo(vector2)
        self.vector_controller.update_by_adding_scalar_repo(2)
        self.assertEqual(self.vector_controller.get_vectors_repo()[0].get_values(), [3, 4])  # 1 + 2, 2 + 2
        self.assertEqual(self.vector_controller.get_vectors_repo()[1].get_values(), [5, 6])  # 3 + 2, 4 + 2
        self.assertEqual(self.vector_controller.get_vectors_repo()[0].sum_of_elements(), 7)  # 3 + 4


if __name__ == '__main__':
    unittest.main()