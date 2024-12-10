from pathlib import Path


class BackupTask:
    def __init__(self, destination_dir: str, source_dir: str | None, files_to_copy: list[str] | None,
                 exclude_files: list[str] | None,
                 exclude_pattern: str | None,
                 is_files_delete_after_copy: bool) -> None:

        # Create path objects for destination and source
        self.destination_dir = Path(destination_dir)
        self.source_dir = Path(source_dir) if source_dir else Path.cwd()

        # Create tuple with specific path files for copy if provided
        self.copy_tuple = tuple([self.source_dir / Path(file) for file in files_to_copy]) if files_to_copy else tuple()

        # Create tuple with exclude path files if provided
        self.exclude_tuple = tuple([self.source_dir / path for path in exclude_files]) if exclude_files else tuple()

        # Set pattern for exclude if provided, set delete flag
        self.exclude_pattern = exclude_pattern
        self.is_delete = is_files_delete_after_copy
