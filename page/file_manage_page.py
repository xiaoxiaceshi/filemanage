import time
from selenium.webdriver.common.by import By
import page
from base.base_action import BaseAction

class FileManagePage(BaseAction):

    # 点击操作菜单
    def click_operate(self):
        self.click(page.operate_button)

    # 点击新建文件夹
    def click_new_folder(self):
        self.click(page.new_folder_button)

    # 点击确定
    def click_confirm(self):
        self.click(page.confirm_button)

    # 输入文件夹/文件名称
    def input_file_name(self,text):
        self.find_element(page.new_file_name_text).clear()
        self.input(page.new_file_name_text, text)

    # 点击父目录,如果找不到，上滑查找父目录
    def click_parent_folder(self):
        self.find_element_with_scroll(page.parent_folder_button, direction ="down").click()

    # 点击新建文件
    def click_new_file(self):
        self.click(page.new_file_button)

    # 点击全部选择
    def click_select_all(self):
        self.click(page.select_all_button)

    # 点击移动选择项
    def click_move_selected(self):
        self.click(page.move_selected_button)

    # 业务组合
    new_folder_list = ["aaa", "zzz"]
    def create_folder(self):
        for i in self.new_folder_list:
            # 点击操作菜单
            self.click_operate()
            # 点击新建文件夹
            self.click_new_folder()
            # 输入新建文件夹名称
            self.input_file_name(i)
            # 点击确定
            self.click_confirm()

        # 新建的文件夹特征
        newed_folder_feature = By.XPATH,"//*[@text='%s']"%(self.new_folder_list[1])
        # 进入zzz文件夹
        self.click(newed_folder_feature)
        time.sleep(2)

    def create_file(self):
        # 循环创建文件
        for i in range(1,21):
            # 点击操作菜单
            self.click_operate()
            # 点击新建文件
            self.click_new_file()
            # 输入新建文件名称
            self.input_file_name(str(i) + ".txt")
            # 点击确定
            self.click_confirm()

    # 全选移动
    def move_files(self):
        # 点击操作菜单
        self.click_operate()
        # 点击全部选择
        self.click_select_all()
        # 点击父目录
        self.click_parent_folder()
        # 进入aaa文件夹
        newed_folder_feature = By.XPATH, "//*[@text='%s']" % (self.new_folder_list[0])
        self.click(newed_folder_feature)
        time.sleep(2)
        # 点击操作菜单
        self.click_operate()
        # 点击移动选择项按钮
        self.click_move_selected()
        time.sleep(5)

    # 获取移动后的文件夹数量（通过全选选择，查看已选择的文件数量判断）
    def get_moved_files_num(self):
        # 点击操作菜单
        self.click_operate()
        # 点击全部选择
        self.click_select_all()
        # 获取数量相关文本
        text = self.get_text(page.selected_files_num)
        # 循环查询字符是否为数字
        str = ""
        for i in text:
            try:
                int(i)
                str = str + i
            except Exception as e:
                pass
        return int(str)