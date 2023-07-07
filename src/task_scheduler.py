import win32com.client


def checkTasksFolderExistsAndDelete(path, skip_prompts):
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    try:
        task_folder = scheduler.GetFolder(path)
        if skip_prompts or input(f"The tasks folder {path} exists but should have been removed. Do you want to delete it? (y/n) ") == 'y':
            for task in task_folder.GetTasks(0):
                task_folder.DeleteTask(task.Name, 0)
            scheduler.DeleteFolder(path)
            print(f' ==> Deleting tasks folder {path}')
    except:
        pass
    scheduler.Disconnect()


def checkTaskExistsAndDelete(path, skip_prompts):
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    try:
        task_folder_path, task_name = path.rsplit("\\", 1)
        task_folder = scheduler.GetFolder(task_folder_path)
        task = task_folder.GetTask(task_name)
        if skip_prompts or input(f"The task {path} exists but should have been removed. Do you want to delete it? (y/n) ") == 'y':
            task_folder.DeleteTask(task_name, 0)
            print(f' ==> Deleting task {path}')
    except:
        pass
    scheduler.Disconnect()