from task_1 import ttest

folderin = "/home/user/tst"
folderout = "/home/user/out"
folderext = "/home/user/folder1"


def test_step1():
    assert ttest(f"cd {folderin}; 7z a {folderout}/arx2", "Everything is Ok"), "test1 FAIL"


def test_step2():
    assert ttest(f"cd {folderout}; 7z e arx2.7z -o{folderext} -y", "Everything is Ok"), "test2 FAIL"


def test_step3():
    assert ttest(f"cd {folderout}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    assert ttest(f"cd {folderout}; 7z d arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step5():
    assert ttest(f"cd {folderin}; 7z u {folderout}/arx2.7z", "Everything is Ok"), "test5 FAIL"


def test_step6():
    res1 = ttest(f"cd {folderin}; 7z a {folderout}/arx2", "Everything is Ok")
    res2 = ttest(f"ls {folderout}", "arx2.7z")
    assert res1 and res2, "test6 FAIL"


def test_step7():
    # test7
    res1 = ttest(f"cd {folderout}; 7z e arx2.7z -o{folderext} -y", "Everything is Ok"), "test7 FAIL"
    res2 = ttest(f"ls {folderext}", "test1.txt")
    res3 = ttest(f"ls {folderext}", "test2.txt")
    assert res1 and res2 and res3, "test7 FAIL"


def test_step8():
    # test8
    assert ttest(f"cd {folderout}; 7z l arx2.7z", "2 files")


def test_step9():
    # test8
    assert ttest(f"cd {folderout}; 7z x arx2.7z -o{folderext} -y", "Everything is Ok"), "test7 FAIL"
