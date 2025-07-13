import logic

def test_add_array():
    v = []
    logic.add_array(v, 5)
    assert v == [5], "Test 1 Failed"
    logic.add_array(v, 10)
    assert v == [5, 10], "Test 2 Failed"
    logic.add_array(v, 0)
    assert v == [5, 10, 0], "Test 3 Failed"
    logic.add_array(v, -2)
    assert v == [5, 10, 0, -2], "Test 4 Failed"
    logic.add_array(v, 100)
    assert v == [5, 10, 0, -2, 100], "Test 5 Failed"
    print("All tests for add_array passed!")

def test_insert_array():
    v = [1, 2, 3]
    logic.insert_array(v, 1, 5)
    assert v == [1, 5, 2, 3], "Test 1 Failed"
    logic.insert_array(v, 0, -1)
    assert v == [-1, 1, 5, 2, 3], "Test 2 Failed"
    logic.insert_array(v, 4, 10)
    assert v == [-1, 1, 5, 2, 3, 10], "Test 3 Failed"
    logic.insert_array(v, 10, 20)  # Should not insert (invalid index)
    assert v == [-1, 1, 5, 2, 3, 10], "Test 4 Failed"
    logic.insert_array(v, 2, 7)
    assert v == [-1, 1, 7, 5, 2, 3, 10], "Test 5 Failed"
    print("All tests for insert_array passed!")

def test_remove_array():
    v = [1, 2, 3, 4]
    logic.remove_array(v, 2)
    assert v == [1, 2, 4], "Test 1 Failed"
    logic.remove_array(v, 0)
    assert v == [2, 4], "Test 2 Failed"
    logic.remove_array(v, 1)
    assert v == [2], "Test 3 Failed"
    logic.remove_array(v, 0)
    assert v == [], "Test 4 Failed"
    logic.remove_array(v, 5)  # Invalid index, should do nothing
    assert v == [], "Test 5 Failed"
    print("All tests for remove_array passed!")

def test_remove_array_index():
    v = [0, 1, 2, 3, 4, 5]
    logic.remove_array_index(v, 1, 3)
    assert v == [0, 4, 5], "Test 1 Failed"
    logic.remove_array_index(v, 0, 1)
    assert v == [4, 5], "Test 2 Failed"
    logic.remove_array_index(v, 0, 0)
    assert v == [5], "Test 3 Failed"
    logic.remove_array_index(v, 0, 1)  # Should not affect as index range is invalid
    assert v == [5], "Test 4 Failed"
    logic.remove_array_index(v, 1, 2)  # Again, should not affect
    assert v == [5], "Test 5 Failed"
    print("All tests for remove_array_index passed!")

def test_replace_array():
    v = [1, 2, 1, 4]
    logic.replace_array(v, 1, 100)
    assert v == [100, 2, 100, 4], "Test 1 Failed"
    logic.replace_array(v, 5, 200)  # Should do nothing
    assert v == [100, 2, 100, 4], "Test 2 Failed"
    logic.replace_array(v, 2, -10)
    assert v == [100, -10, 100, 4], "Test 3 Failed"
    logic.replace_array(v, 100, 50)
    assert v == [50, -10, 100, 4], "Test 4 Failed"
    logic.replace_array(v, 4, 4)  # Should do nothing as not present
    assert v == [50, -10, 100, 4], "Test 5 Failed"
    print("All tests for replace_array passed!")

def test_prime_array():
    v=[1,2,3,4,5]
    logic.prime_array(v,0,4)
    assert v==[2,3,5],"Test 1 Failed"
    v=[1,1,4,4,2,3,10,5]
    logic.prime_array(v,3,7)
    assert v==[1,1,4,2,3,5],"Test 2 Failed"
    v=[2,2,4,4,6,7]
    logic.prime_array(v,2,4)
    assert v==[2,2,7], "Test 3 Failed"
    print("All tests for prime_array passed!")
    v=[2,2,80,80,100,3,5]
    logic.prime_array(v,0,4)
    assert v==[2,2,3,5],"Test 4 Failed"
    v=[1,3,5,7,11]
    logic.prime_array(v,0,4)
    assert v==[3,5,7,11],"Test 5 Failed"

def test_odds_array():
    v=[1,2,3,4,5]
    logic.odd_array(v,0,4)
    assert v==[1,3,5],"Test 1 Failed"
    v=[1,1,4,4,2,3,10,5]
    logic.odd_array(v,3,7)
    assert v==[1,1,4,3,5],"Test 2 Failed"
    v=[2,2,4,4,6,7]
    logic.odd_array(v,0,5)
    assert v==[7], "Test 3 Failed"
    v=[1,3,5,11]
    logic.odd_array(v,0,3)
    assert v==[1,3,5,11],"Test 4 Failed"
    v=[2,2,4,4,6]
    logic.odd_array(v,0,4)
    assert v==[], "Test 5 Failed"
    print("All tests for odd_array passed!")

def test_sum_array():
    v=[1,2,3,4,5]
    s=logic.sum_array(v,0,4)
    assert s==15, "Test 1 Failed"
    v=[1,1,4,4,2,3,10,5]
    s=logic.sum_array(v,3,7)
    assert s==24, "Test 2 Failed"
    v=[100,600,2300,1,2,3,1000]
    s=logic.sum_array(v,3,5)
    assert s==6, "Test 3 Failed"
    v=[2,2,4,4,6,7]
    s=logic.sum_array(v,0,4)
    assert s==18, "Test 4 Failed"
    v=[1,3,5,7,11]
    s=logic.sum_array(v,3,4)
    assert s==18, "Test 5 Failed"
    print("All tests for sum_array passed!")

def test_gcd_array():
    v=[1,2,3,4,5]
    g=logic.gcd_array(v,0,4)
    assert g==1, "Test 1 Failed"
    v=[4,8,16]
    g=logic.gcd_array(v,0,2)
    assert g==4, "Test 2 Failed"
    v=[10,50,20]
    g=logic.gcd_array(v,0,2)
    assert g==10, "Test 3 Failed"
    v=[6,3,9]
    g=logic.gcd_array(v,0,2)
    assert g==3, "Test 4 Failed"
    v=[9,81,3,6]
    g=logic.gcd_array(v,0,3)
    assert g==3, "Test 5 Failed"
    print("All tests for gcd_array passed!")

def test_max_array():
    v=[1,2,3,4,5]
    m=logic.max_array(v,0,4)
    assert m==5, "Test 1 Failed"
    v=[100,500,1]
    m=logic.max_array(v,0,2)
    assert m==500, "Test 2 Failed"
    v=[2,128,5]
    m=logic.max_array(v,0,2)
    assert m==128, "Test 3 Failed"
    v=[100,120,999]
    m=logic.max_array(v,0,2)
    assert m==999, "Test 4 Failed"
    v=[1,2,34,312,12412]
    m=logic.max_array(v,0,4)
    assert m==12412, "Test 5 Failed"
    print("All tests for max_array passed!")

def test_filter_prime():
    v=[1,2,3,4,5]
    logic.filter_prime(v)
    assert v==[2,3,5],"Test 1 Failed"
    v=[37,8,9,3]
    logic.filter_prime(v)
    assert v==[37,3],"Test 2 Failed"
    v=[2,2,2,68]
    logic.filter_prime(v)
    assert v==[2,2,2],"Test 3 Failed"
    v=[3,3,1,0,9]
    logic.filter_prime(v)
    assert v==[3,3],"Test 4 failed"
    v=[100,200,8]
    logic.filter_prime(v)
    assert v==[],"Test 5 failed"
    print("All tests for filter_prime passed!")

def filter_negative():
    v=[1,2,3,4,5]
    logic.filter_negative(v)
    assert v==[],"Test 1 Failed"
    v=[-1,-2,3,5]
    logic.filter_negative(v)
    assert v==[-1,-2],"Test 2 Failed"
    v=[19,20,-19]
    logic.filter_negative(v)
    assert v==[-19],"Test 3 Failed"
    v=[-2189,10,-2931]
    logic.filter_negative(v)
    assert v==[-2189,-2931],"Test 4 Failed"
    v=[310,-319,-2]
    logic.filter_negative(v)
    assert v==[-319,-2],"Test 5 Failed"
    print("All tests for filter_negative passed!")
