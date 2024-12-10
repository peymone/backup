from src.backup import LocalBackuper
from src.config import configurator
from src.prettify import prettifier
from src.log import logger


def show_task_data(task_data: dict):
    for name, value in task_data.items():
        prettifier.print(name, style="help", end=": ", show_time=False)
        prettifier.print(value, style="data", show_time=False)

        logger.info(f"{name}: {value}")


if __name__ == "__main__":
    tasks_data: list[dict] = configurator.get_tasks_data()
    prettifier.print(f"Tasks in pool: {len(tasks_data)}", style="info", end="\n\n")
    logger.info(f"Tasks in pool: {len(tasks_data)}")

    if len(tasks_data) > 0:
        for data in tasks_data:

            backuper = LocalBackuper(
                destination_dir=data.get("destination"),
                source_dir=data.get("source"),
                files_to_copy=data.get("file_list"),
                exclude_files=data.get("exclude_list"),
                exclude_pattern=data.get("exclude_pattern"),
                is_files_delete_after_copy=data.get("remove_flag")
            )

            prettifier.print("Start backup operation for task:", style="info")
            logger.info("Start backup operation for task:")
            show_task_data(data)

            status_code, result_msg = backuper.backup()

            if status_code is True:
                prettifier.print(result_msg, style="sucess")
                logger.info(result_msg)
            else:
                prettifier.print(result_msg, style="warning")
                logger.warning(result_msg)

            print("\n")
    else:
        prettifier.print("Program was executed without backup", style="sucess")
        logger.info("Program was executed without backup")
