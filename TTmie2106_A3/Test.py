from Point import MyPoint
from PointRepository import PointRepository

def test_my_point():
    # Test point creation
    p1 = MyPoint(3, 4, 'red')
    assert p1.get_coord_x() == 3
    assert p1.get_coord_y() == 4
    assert p1.get_color() == 'red'
    assert isinstance(p1, MyPoint)  # Ensure p1 is an instance of MyPoint
    assert p1.distance(MyPoint(0, 0, 'red')) == 5.0  # Check distance from (3,4) to (0,0)

    # Test point string representation
    assert str(p1) == "Point (3,4) of color red"
    assert 'Point' in str(p1)  # Ensure the string contains 'Point'

    # Test distance calculation between two points
    p2 = MyPoint(0, 0, 'blue')
    assert p1.distance(p2) == 5.0  # Distance from (3,4) to (0,0)
    assert p1.distance(p1) == 0.0  # Distance from a point to itself
    assert p1.distance(MyPoint(3, 0, 'blue')) == 4.0  # Check distance to another point directly below

def test_point_repository():

    PR = PointRepository([])

    # Test adding points
    p1 = MyPoint(1, 2, 'red')
    p2 = MyPoint(3, 4, 'green')
    PR.add_point(p1)
    PR.add_point(p2)
    assert len(PR.get_points()) == 2
    assert PR.get_points() == [p1, p2]  # Ensure both points are added
    assert PR.get_points()[0].get_color() == 'red'  # Check the color of the first point
    assert PR.get_points()[1].get_coord_y() == 4  # Check the y-coordinate of the second point
    assert isinstance(PR.get_points()[1], MyPoint)  # Ensure it's an instance of MyPoint

    # Test getting points
    assert PR.get_point_at_index(0) == p1
    assert PR.get_point_at_index(1) == p2
    assert PR.get_points()[0].get_coord_x() == 1  # Check x-coordinate of first point
    assert PR.get_points()[1].get_color() == 'green'  # Check color of second point
    assert len(PR.get_points()) == 2  # Ensure the number of points remains unchanged

    # Test getting points of a given color
    red_points = PR.get_points_of_color('red')
    assert len(red_points) == 1
    assert red_points[0] == p1
    assert red_points[0].get_color() == 'red'  # Check if the color of the red point is correct
    assert PR.get_points_of_color('blue') == []  # Ensure color not in points returns an empty list
    assert len(PR.get_points_of_color('green')) == 1  # Ensure green points match expected count

    # Test minimum distance
    assert PR.minimum_distance() == 2.8284271247461903  # Distance between p1 and p2
    assert PR.minimum_distance() > 0  # Ensure it's positive
    assert isinstance(PR.minimum_distance(), float)  # Ensure it's a float

    # Test updating a point
    p3 = MyPoint(5, 5, 'yellow')
    PR.update_at_index(1, p3)
    assert PR.get_point_at_index(1) == p3
    assert PR.get_point_at_index(1).get_color() == 'yellow'  # Ensure the color is updated
    assert PR.get_point_at_index(1).get_coord_x() == 5  # Ensure the x-coordinate is updated
    assert len(PR.get_points()) == 2  # Confirm the size remains unchanged

    # Test deleting a point
    PR.delete_at_index(0)
    assert len(PR.get_points()) == 1  # Only p3 should remain
    assert PR.get_points()[0] == p3  # Check the remaining point is p3
    assert PR.get_points() != [p1]  # Ensure p1 was actually removed
    assert PR.get_points()[0].get_coord_y() == 5  # Ensure it has the correct y-coordinate

    # Test getting points inside a square
    square_points = PR.get_points_inside_square(MyPoint(5, 5, 'yellow'), 2)
    assert len(square_points) == 1  # p3 should be in the square
    assert square_points[0] == p3  # Ensure the point matches p3
    assert PR.get_points_inside_square(MyPoint(1, 1, 'red'), 1) == []  # No points should be here

    # Test deleting points inside a square
    PR.delete_points_inside_square(MyPoint(4, 6, 'green'), 3)
    assert len(PR.get_points()) == 0  # All points should be deleted
    assert PR.get_points() == []  # Ensure no points remain


if __name__ == "__main__":
    test_my_point()
    test_point_repository()
    print("All tests passed!")