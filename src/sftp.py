import pysftp

from src.config import configurator


class SFTPClient:
    def get_connection(self):
        sftp_connection = pysftp.Connection(
            host=configurator.sftp_host,
            port=configurator.sftp_port,
            username=configurator.sftp_user,
            password=configurator.sftp_password
        )

        return sftp_connection


sftp_client = SFTPClient()
