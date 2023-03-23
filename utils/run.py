import os
import allure
import pytest



# --clean-alluredir:每次执行前清空数据，这样在生成的报告中就不会追加，只显示当前执行的用例
if __name__ == '__main__':
    pytest.main(['-s', '-q',r'D:\PycharmProjects\pytest\testcases\test_demo.py','--clean-alluredir',r'--alluredir=allure-results'])
    os.system(r"allure generate -c -o allure-report")