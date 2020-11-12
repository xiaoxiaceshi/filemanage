from base.base_driver import BaseDriver
from page.file_manage_page import FileManagePage

class TestFileManage:
    def setup(self):
        self.driver = BaseDriver().get_driver()
        print("获取驱动成功")
        self.FileManagePage = FileManagePage(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_file_manage(self):
        self.FileManagePage.create_folder()
        self.FileManagePage.create_file()
        self.FileManagePage.move_files()
        num = self.FileManagePage.get_moved_files_num()
        print(num)
        assert num == 20
    
    def test_1(self):
        print(1)
        assert 1
        
    def test_2(self):
        print(2)
        assert 0
        
    def test_3(self):
        print(3)
        assert 0
        
    def test_4(self):
        print(4)
        assert 1

    def test_chizi(self):
        print("丹丹lllll")
        print("哈哈哈哈")
        assert 1
