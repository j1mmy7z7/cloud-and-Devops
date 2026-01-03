
import os
import datetime as dt
import tarfile
import subprocess

FORMAT_TIME_STRING: str = "[%d/%m/%Y-%H:%M]"
ARCHIVE: str  = f'/backup/{dt.datetime.now().strftime("%d-%m-%Y_%H-%M")}_wordpress_backup.tar'
BACKUP_FILE_NAME: str = "wordpress_backup.sql"
BACKUP_FILE: str = f"/home/jmuchiri/.opt/{BACKUP_FILE_NAME}"
DATABASE: str = "wordpress_db"
LOG_FILE: str = "/var/log/backup.log"

def run_backup():
    command = ["mysqldump", "--defaults-group-suffix=backup", DATABASE]
    try:
        result = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True,
                )
        with open(BACKUP_FILE, "w") as f:
            f.write(result.stdout)
        log("Backup sql created from mysql server")
        # archive the file here
        archive_file(BACKUP_FILE_NAME)
    except subprocess.CalledProcessError as e:
        log(f"Backup sql file creation failed. Error: {e.stderr.decode()}")
    except Exception as e:
        log(f"Unexpected error: {e}")


def archive_file(filename: str):
    try:
        with tarfile.open(ARCHIVE, mode="w") as tar_file:
            tar_file.add(BACKUP_FILE)
        log("Backup archive created successfully")
        os.remove(BACKUP_FILE)
    except Exception as e:
        message: str = f"archive of {filename} failed, error is {e}"
        log(message)
        # remove file if created
        os.remove(BACKUP_FILE)


def log(log: str):
    log_message: str = dt.datetime.now().strftime(FORMAT_TIME_STRING) + ": " + log + "\n"
    with open(LOG_FILE, "a") as file:
        file.write(log_message)

if __name__ == "__main__":
    run_backup()
