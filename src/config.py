from configparser import ConfigParser
from argparse import ArgumentParser
from json import dump, load
from os.path import exists, getsize


class Configurator:
    def __init__(self) -> None:
        """Load config, create save file if not exist, read terminal arguments"""

        self.__task_list = list()
        self.__load_config(config_path="./settings/config.ini")
        self.__create_save_file()
        self.__read_terminal_arguments()

        self.time_format: str = "%Y-%m-%d %H:%M:%S"

    def get_tasks_data(self) -> list[dict]:
        return self.__task_list

    def __load_config(self, config_path: str) -> None:
        parser = ConfigParser()
        parser.read(config_path)

        self.save_file = parser['PROD'].get("SAVE_PATH_FOR_TASKS")
        self.logs_file = parser['PROD'].get("SAVE_PATH_FOR_LOGS")
        self.max_workers = parser['PROD'].getint("MAX_WORKERS")

        self.sftp_host = parser["SFTP"].get("HOST")
        self.sftp_port = parser["SFTP"].getint("PORT")
        self.sftp_user = parser["SFTP"].get("USER")
        self.sftp_password = parser["SFTP"].get("PASSWORD")

    def __create_save_file(self) -> None:
        if exists(self.save_file):
            pass
        else:
            file = open(self.save_file, "x")
            file.close()

    def __read_terminal_arguments(self) -> None:
        parser = ArgumentParser()
        parser.add_argument("-s", "--source", help="path to source directory", type=str)
        parser.add_argument("-d", "--destination", help="path to destination directory", type=str)
        parser.add_argument("-f", "--files", help="choose files to backup, example: 'my.txt your.txt'", type=str)
        parser.add_argument("-e", "--exclude", help="exclude files from backup, example: 'my.txt your.txt'", type=str)
        parser.add_argument("-p", "--pattern", help="exclude pattern from backup, example: '*.txt photo.jpg'", type=str)
        parser.add_argument("-r", "--remove", help="delete files after backup", default=False, type=bool)
        parser.add_argument("-sb", "--saveb", help="save current task with backup", default=False, type=bool)
        parser.add_argument("-sw", "--savew", help="save current task without backup", default=False, type=bool)

        args = parser.parse_args()
        task_data = dict()

        # Parse terminal arguments in task data if provided
        if args.destination:
            task_data['source'] = args.source
            task_data['destination'] = args.destination
            task_data['file_list'] = args.files.split() if args.files else None
            task_data['exclude_list'] = args.exclude.split() if args.exclude else None
            task_data['exclude_pattern'] = args.pattern
            task_data['remove_flag'] = args.remove

            # Check save flags
            if args.savew or args.saveb:
                self.__update_save_file(task_data)

            if args.savew:
                return
            else:
                self.__task_list.append(task_data)
        else:
            self.__task_list = self.__read_save_file()

    def __read_save_file(self) -> list[dict]:
        if getsize(self.save_file) != 0:
            with open(self.save_file, "r") as file:
                return load(file)
        else:
            return list()

    def __update_save_file(self, task_data: dict) -> None:
        save_file_data = self.__read_save_file()
        save_file_data.append(task_data)

        with open(self.save_file, "w") as file:
            dump(save_file_data, file, indent=4)


configurator = Configurator()
