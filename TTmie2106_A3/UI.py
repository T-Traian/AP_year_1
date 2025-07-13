
from Logic import *

def main():
    PR=PointRepository(list=[])
    while True:
        choice=show_meniu()
        if choice=='1':
            list=PR.get_points()
            try:
                if len(list) != 0:
                    raise Exception("The list already has elements.")
                else:
                    print()
                    n = int(input("Enter how many points would you like to read:"))
                    PR = PointRepository(read_list(n))
            except Exception as e:
                print(f"The error is: {e}")
        else:
            if choice=='2':
                PR.add_point(read_point())
            else:
                if choice=='3':
                    print()
                    list=PR.get_points()
                    if len(list)!=0:
                        print("The points in the list are: ")
                        for i in list:
                            print(i)
                    else:
                        print("The list is empty. Please add points.")
                else:
                    if choice=='4':
                        index=read_index()
                        po=PR.get_point_at_index(index)
                        print("At index there is the",po)
                    else:
                        if choice=='5':
                            color=read_color()
                            list_point=PR.get_points()
                            if len(list_point)!=0:
                                list = PR.get_points_of_color(color)
                                if len(list) != 0:
                                    print()
                                    print("The following points have the same color:")
                                    for i in list:
                                        print(i)
                                else:
                                    print("There are no such points.")
                            else:
                                print("The list is empty. Please add points.")
                        else:
                            if choice=='6':
                                lenght=read_lenght()
                                po=read_point()
                                list=PR.get_points_inside_square(po,lenght)
                                if len(list)!=0:
                                    print()
                                    print("The points are:")
                                    for i in list:
                                        print(i)
                                else:
                                    print()
                                    print("There are no such points.")
                            else:
                                if choice=='7':
                                    nr=PR.minimum_distance()
                                    print("The minimum distance is",nr)
                                else:
                                    if choice=='8':
                                        index=read_index()
                                        point=read_point()
                                        PR.update_at_index(index,point)
                                    else:
                                        if choice=='9':
                                            index=read_index()
                                            PR.delete_at_index(index)
                                        else:
                                            if choice=='10':
                                                point=read_point()
                                                lenght=read_lenght()
                                                list=PR.delete_points_inside_square(point,lenght)
                                            else:
                                                if choice=='11':
                                                    max=PR.maximum_distance()
                                                    print("The maximum distance is:",max)
                                                else:
                                                    if choice=='12':
                                                        PR.shift_on_y()
                                                    else:
                                                        if choice=='13':
                                                            distance=read_distance()
                                                            point=read_point()
                                                            PR.delete_all_points_within_distance(point,distance)
                                                        else:
                                                            if choice=='14':
                                                                try:
                                                                    point_list = PR.get_points()
                                                                    if len(point_list) != 0:
                                                                        plot_points(PR)
                                                                    else:
                                                                        raise ValueError("The list of points is empty.")
                                                                except ValueError as e:
                                                                    print(f"The error is: {e}")



if __name__ == '__main__':
    main()