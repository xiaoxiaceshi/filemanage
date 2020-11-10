from base.base_driver import BaseDriver
from page.file_manage_page import FileManagePage

class TestFileManage:
    # 初始化
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
