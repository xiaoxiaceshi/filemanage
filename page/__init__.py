from selenium.webdriver.common.by import By

# 操作按钮
operate_button = By.ID,"com.cyanogenmod.filemanager:id/ab_actions"

# 新建文件夹按钮
new_folder_button = By.XPATH,"//*[@text='新建文件夹']"

# 新建文件夹/文件名称输入框
new_file_name_text = By.ID,"com.cyanogenmod.filemanager:id/input_name_dialog_edit"

# 确定按钮
confirm_button = By.XPATH,"//*[@text='确定']"

# 父目录
parent_folder_button =  By.XPATH,"//*[@text='父目录']"

# 新建文件按钮
new_file_button = By.XPATH,"//*[@text='新建文件']"

# 全部选择按钮
select_all_button = By.XPATH,"//*[@text='全部选择']"

# 移动选择项按钮
move_selected_button = By.XPATH,"//*[@text='移动选择项']"

# 已选择文件数量(文本，里面包含数量)
selected_files_num = By.ID,"com.cyanogenmod.filemanager:id/navigation_status_selection_label"