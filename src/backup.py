# Built in modules
from pathlib import Path
from shutil import copy
from re import search
from typing import Generator
from concurrent.futures import ThreadPoolExecutor

# My modules
from src.models import BackupTask
from src.log import logger
from src.sftp import sftp_client
from src.config import configurator


class LocalBackuper(BackupTask):
    def backup(self) -> tuple[bool, str]:
        """Copy files from source to destination directory, delete files after copied if provided specific flag

        Returns:
            tuple[bool, str]: code result (True - if operation was successful, False otherwise), operation description
        """

        if not self.__is_source_dir_exist() and not self.__is_destination_dir_exist():
            return False, "Directories for backup do not exist"

        if not self.__is_files_to_copy_exist():
            return False, "Some files for copy do not exist"

        # Copy files from source to destination directory
        with ThreadPoolExecutor(configurator.max_workers) as executor:
            for file in self.__get_files_to_copy():
                executor.submit(lambda file: copy(file, self.destination_dir), file)
                logger.debug("copy file " + str(file))

        self.__delete_files_in_source_dir()
        return True, "Backup operation was completed without errors"

    def __is_source_dir_exist(self) -> bool:
        return True if self.source_dir.exists() else False

    def __is_destination_dir_exist(self) -> bool:
        return True if self.destination_dir.exists() else False

    def __is_files_to_copy_exist(self) -> bool:
        if self.copy_tuple:
            return all([file.exists() for file in self.copy_tuple])
        else:
            return True

    def __is_file_need_to_copy(self, file_path: Path) -> bool:
        if self.exclude_pattern and search(self.exclude_pattern, file_path.name):
            return False

        if file_path in self.exclude_tuple:
            return False

        return True

    def __get_files_to_copy(self) -> Generator:
        paths_to_copy = self.copy_tuple if self.copy_tuple else tuple(self.source_dir.iterdir())

        for file_path in paths_to_copy:
            if self.__is_file_need_to_copy(file_path):
                yield file_path

    def __delete_files_in_source_dir(self) -> None:
        if self.is_delete:
            with ThreadPoolExecutor(configurator.max_workers) as executor:
                executor.map(lambda file_path: file_path.unlink(), self.__get_files_to_copy())


class RemoteBackup(LocalBackuper):
    def backup(self):
        if not self.__is_source_dir_exist():
            return False, "Source directory do not exist"

        if not self.__is_files_to_copy_exist():
            return False, "Some files for copy do not exist"

        sftp_connection = sftp_client.get_connection()

        for file in self.__get_files_to_copy():
            sftp_connection.put(file, self.destination_dir)

        self.__delete_files_in_source_dir()
        return True, "Backup operation was completed without errors"
