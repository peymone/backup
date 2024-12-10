<h1 align="center">Files Backup System</h1>

<p align="center">
    <img src="https://img.shields.io/badge/%20Python-3.11.3-blue?style=for-the-badge&logo=Python" alt="Python">
    <img src="https://img.shields.io/badge/%20Rich-13.9.4-brightgreen?style=for-the-badge" alt="Rich">
    <img src="https://img.shields.io/badge/%20PySFTP-0.2.9-brightgreen?style=for-the-badge" alt="PySFTP">
</p>
<p align="center">
    <img src="https://img.shields.io/github/downloads/peymone/backup/total?style=social&logo=github" alt="downloads">
    <img src="https://img.shields.io/github/watchers/peymone/backup" alt="watchers">
    <img src="https://img.shields.io/github/stars/peymone/backup" alt="stars">
</p>

<h2>About</h2>

File backup system to local or remote storage through SFTP server. Implemented features:

- [x] _Load config from "config.ini" file_
- [x] _Read terminal arguments_
- [x] _Backup for local destination_
  - [x] _Copy all files from source to destination directory:_ ```python run.py -s C:/source_dir -d D:/destination_dir```
  - [x] _Copy only specific files:_ ```python run.py -s C:/source_dir -d D:/destination_dir -f 'test.txt test.jpg'```
  - [x] _Copy everything except excluded files:_ ```python run.py -s C:/source_dir -d D:/destination_dir -e test.txt```
  - [x] _Copy everything except files with pattern:_ ```python run.py -s C:/source_dir -d D:/destination_dir -p *.txt```
  - [x] _Delete files after backup:_ ```python run.py -s C:/source_dir -d D:/destination_dir -r 1```
  - [x] _Save task to json file and do backup:_ ```python run.py -s C:/source_dir -d D:/destination_dir -sb 1```
  - [x] _Save task to json file and skip backup:_ ```python run.py -s C:/source_dir -d D:/destination_dir -sw 1```
  - [x] _Automate backup from saved tasks:_ ```python run.py```
- [ ] _Backup for remote destination through SFTP server_
