import unittest
from Domain.Passenger import Passenger
from Infrastructure.Plane import Plane
from Infrastructure.PlaneRepository import PlaneRepository
from Application.PlaneController import PlaneController


class TestPlaneController(unittest.TestCase):

    def test_sort_passengers_by_last_name(self):
        # Create sample passengers and a plane
        passenger1 = Passenger("Alice", "Smith", "ABC123")
        passenger2 = Passenger("Bob", "Johnson", "ABC456")
        plane = Plane("Flight1", "AirlineA", 150, "NYC", [passenger1, passenger2])
        plane_repo = PlaneRepository([plane])
        plane_controller = PlaneController(plane_repo)

        plane_controller.sort_passengers_by_lastName_repo("Flight1")
        sorted_passengers = plane.get_passengers()

        self.assertEqual(sorted_passengers[0].get_last_name(), "Johnson")  # Bob should come before Alice
        self.assertEqual(sorted_passengers[1].get_last_name(), "Smith")  # Alice should be after Bob
        self.assertEqual(len(sorted_passengers), 2)  # There are 2 passengers

    def test_sort_planes_number_of_passengers(self):
        # Create sample planes with varying passenger counts
        passenger1 = Passenger("Alice", "Smith", "ABC123")
        passenger2 = Passenger("Bob", "Johnson", "ABC456")
        plane1 = Plane("Flight1", "AirlineA", 150, "NYC", [passenger1])
        plane2 = Plane("Flight2", "AirlineB", 200, "LA", [passenger2, Passenger("Charlie", "Brown", "XYZ123")])

        plane_repo = PlaneRepository([plane1, plane2])
        plane_controller = PlaneController(plane_repo)

        plane_controller.sort_planes_number_of_passengers_repo()
        sorted_planes = plane_repo.get_planes()

        self.assertEqual(sorted_planes[0].get_name_number(), "Flight1")  # Flight without Charlie should come first
        self.assertEqual(len(sorted_planes), 2)  # There are 2 planes

    def test_sort_planes_by_count_with_first_name_substring(self):
        # Create sample passengers and planes
        passenger1 = Passenger("Alice", "Smith", "ABC123")
        passenger2 = Passenger("Andre", "Johnson", "ABC456")
        plane1 = Plane("Flight1", "AirlineA", 150, "NYC", [passenger1])
        plane2 = Plane("Flight2", "AirlineB", 200, "LA", [passenger2])

        plane_repo = PlaneRepository([plane1, plane2])
        plane_controller = PlaneController(plane_repo)

        # Sort based on substring
        plane_controller.sort_planes_number_of_passengers_first_name_repo("A")
        sorted_planes = plane_repo.get_planes()

        self.assertEqual(sorted_planes[0].get_name_number(), "Flight1")  # Should come first as it has Alice
        self.assertEqual(len(sorted_planes), 2)

    def test_sort_planes_concatenation(self):
        # Create sample planes with different number of passengers and destinations
        passenger1 = Passenger("Alice", "Smith", "ABC123")
        passenger2 = Passenger("Bob", "Johnson", "ABC456")
        plane1 = Plane("Flight1", "AirlineA", 150, "NYC", [passenger1])
        plane2 = Plane("Flight2", "AirlineB", 200, "LA", [passenger2, Passenger("Charlie", "Brown", "XYZ123")])

        plane_repo = PlaneRepository([plane1, plane2])
        plane_controller = PlaneController(plane_repo)

        plane_controller.sort_planes_concatenation_repo()
        sorted_planes = plane_repo.get_planes()

        self.assertEqual(sorted_planes[0].get_name_number(), "Flight1")  # Should be first as it's the only 1 passenger
        self.assertEqual(sorted_planes[1].get_name_number(), "Flight2")  # More passengers than Flight1

    def test_identify_planes_with_same_passport_number_start(self):
        # Create sample planes with passengers having the same passport number start
        passenger1 = Passenger("Alice", "Smith", "ABC123")
        passenger2 = Passenger("Bob", "Johnson", "ABC456")
        plane1 = Plane("Flight1", "AirlineA", 150, "NYC", [passenger1])
        plane2 = Plane("Flight2", "AirlineB", 200, "LA", [passenger2])

        plane_repo = PlaneRepository([plane1, plane2])
        plane_controller = PlaneController(plane_repo)

        planes = plane_controller.identify_planes_passport_numbers_repo()

        self.assertEqual(len(planes), 2)  # Both planes should be included
        self.assertIn(plane1, planes)
        self.assertIn(plane2, planes)

    def test_identify_passengers_with_string_in_name(self):
        # Create sample passengers and a plane
        passenger1 = Passenger("Alice", "Smith", "ABC123")
        passenger2 = Passenger("Bob", "Johnson", "ABC456")
        plane = Plane("Flight1", "AirlineA", 150, "NYC", [passenger1, passenger2])

        plane_repo = PlaneRepository([plane])
        plane_controller = PlaneController(plane_repo)

        # Find passengers with 'li' in their first or last names
        passengers = plane_controller.identify_passengers_from_plane_repo(plane, "li")

        self.assertEqual(len(passengers), 1)  # Only Alice matches
        self.assertEqual(passengers[0].get_first_name(), "Alice")

    def test_identify_planes_with_given_passenger_name(self):
        # Create sample passengers and a plane
        passenger1 = Passenger("Alice", "Smith", "ABC123")
        plane = Plane("Flight1", "AirlineA", 150, "NYC", [passenger1])

        plane_repo = PlaneRepository([plane])
        plane_controller = PlaneController(plane_repo)

        # Identify planes with the passenger "Alice Smith"
        planes = plane_controller.identify_planes_passenger_given_name_repo("Alice", "Smith")

        self.assertEqual(len(planes), 1)  # Only one plane should have this passenger
        self.assertEqual(planes[0].get_name_number(), "Flight1")

    def test_form_groups_of_k_passengers(self):
        # Create sample passengers and a plane
        passenger1 = Passenger("Alice", "Smith", "ABC123")
        passenger2 = Passenger("Bob", "Johnson", "ABC456")
        plane = Plane("Flight1", "AirlineA", 150, "NYC", [passenger1, passenger2])

        plane_repo = PlaneRepository([plane])
        plane_controller = PlaneController(plane_repo)

        # Form groups of 2 passengers
        passenger_groups = list(plane_controller.callBKT_diff_last_name_repo(2, "Flight1"))

        self.assertEqual(len(passenger_groups), 1)  # One group should be formed
        self.assertEqual(passenger_groups[0][0].get_first_name(), "Alice")  # Validate the first passenger in the group
        self.assertEqual(passenger_groups[0][1].get_first_name(), "Bob")  # Validate the second passenger in the group

    def test_form_groups_of_k_planes(self):
        # Create sample planes with different destinations
        plane1 = Plane("Flight1", "AirlineA", 150, "NYC", [])
        plane2 = Plane("Flight2", "AirlineB", 200, "NYC", [])

        plane_repo = PlaneRepository([plane1, plane2])
        plane_controller = PlaneController(plane_repo)

        # Form groups of 2 planes
        plane_groups = list(plane_controller.callBKT_planes(2))

        self.assertEqual(len(plane_groups), 1)  # One group should be formed
        self.assertEqual(plane_groups[0][0].get_name_number(), "Flight1")  # Validate the first plane in the group
        self.assertEqual(plane_groups[0][1].get_name_number(), "Flight2")  # Validate second plane in the group


if __name__ == "__main__":
    unittest.main()