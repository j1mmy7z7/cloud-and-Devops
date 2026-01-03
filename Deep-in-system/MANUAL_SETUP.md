# Manual Server Setup & WordPress Deployment

This guide details the steps to manually provision the Ubuntu server, replicating the automation provided by the Ansible playbook.

## Prerequisites

*   **Target Machine**: A clean Ubuntu Server installation.
*   **Root Access**: You must be able to run commands as `root` (via `sudo -i` or directly).

## 1. Network Configuration

### Configure Static IP (Netplan)
1.  Identify your network interface name (e.g., `eth0`, `ens3`) using `ip addr`.
2.  Create or edit the Netplan configuration file:
    ```bash
    sudo nano /etc/netplan/50-cloud-init.yaml
    ```
3.  Add your configuration (replace placeholders):
    ```yaml
    network:
      version: 2
      renderer: networkd
      ethernets:
        YOUR_INTERFACE_NAME:
          dhcp4: no
          addresses:
            - YOUR_STATIC_IP/24
          routes:
            - to: default
              via: YOUR_GATEWAY_IP
          nameservers:
            addresses: [8.8.8.8, 1.1.1.1]
    ```
4.  Apply the changes:
    ```bash
    sudo netplan apply
    ```
5.  Verify connectivity: `ping -c 4 google.com`

## 2. Security & Firewall (UFW)

1.  **Install UFW**:
    ```bash
    sudo apt update
    sudo apt install ufw
    ```
2.  **Set Defaults**:
    ```bash
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    ```
3.  **Allow Necessary Ports**:
    ```bash
    # SSH (Custom Port)
    sudo ufw allow 2222/tcp
    # HTTP
    sudo ufw allow 80/tcp
    # FTP Control
    sudo ufw allow 21/tcp
    # FTP Passive Range (Example: 40000-50000)
    sudo ufw allow 40000:50000/tcp
    ```
4.  **Enable Firewall**:
    ```bash
    sudo ufw enable
    ```

## 3. User Management

### Create Users
1.  **Luffy (Admin)**:
    ```bash
    sudo useradd -m -s /bin/bash luffy
    sudo usermod -aG sudo luffy # Grant sudo privileges
    sudo passwd luffy
    # Setup SSH Key for Luffy manually by copying your public key to /home/luffy/.ssh/authorized_keys
    ```
2.  **Zoro (Standard)**:
    ```bash
    sudo useradd -m -s /bin/bash zoro
    sudo passwd zoro
    ```
3.  **Nami (Backup)**:
    ```bash
    sudo useradd -m -d /backup -s /usr/sbin/nologin nami
    sudo passwd nami
    # Ensure /backup directory exists and has correct permissions
    sudo mkdir -p /backup
    sudo chown nami:nami /backup
    ```

### SSH Hardening
Edit `/etc/ssh/sshd_config`:
```bash
sudo nano /etc/ssh/sshd_config
```
Changes to make:
```ssh
Port 2222
PermitRootLogin no
PasswordAuthentication yes
PubkeyAuthentication yes

# Append to end of file
Match User luffy
    PasswordAuthentication no
    AuthenticationMethods publickey
```
Restart SSH:
```bash
sudo systemctl daemon-reload
sudo systemctl Restart ssh.socket
```

## 4. Services Stack

### FTP (vsftpd)
1.  **Install**: `sudo apt install vsftpd`
2.  **Configure**: Edit `/etc/vsftpd.conf`:
    ```ini
    anonymous_enable=NO
    local_enable=YES
    write_enable=YES
    chroot_local_user=YES
    allow_writeable_chroot=YES
    pasv_min_port=40000
    pasv_max_port=50000
    ```
3.  **Restart**: `sudo systemctl restart vsftpd`

### MySQL
1.  **Install**: `sudo apt install mysql-server python3-pymysql`
2.  **Secure Installation**: Run `sudo mysql_secure_installation`.
3.  **Bind to Localhost**: Edit `/etc/mysql/mysql.conf.d/mysqld.cnf` and set `bind-address = 127.0.0.1`.
4.  **Create Database & User**:
    ```sql
    sudo mysql -u root -p
    -- Inside MySQL shell:
    CREATE DATABASE wordpress_db;
    CREATE USER 'wp_user'@'localhost' IDENTIFIED BY 'STRONG_PASSWORD';
    GRANT ALL PRIVILEGES ON wordpress_db.* TO 'wp_user'@'localhost';
    GRANT PROCESS, SELECT, LOCK TABLES, SHOW VIEW ON *.* TO 'wp_user'@'localhost';
    FLUSH PRIVILEGES;
    EXIT;
    ```
5.  **Create Root Config**: Create `/root/.my.cnf`:
    ```ini
    [client]
    user=root
    password=YOUR_ROOT_MYSQL_PASSWORD
    ```

### Nginx & PHP
1.  **Install**:
    ```bash
    sudo apt install nginx php8.3-cli php8.3-fpm php8.3-mysql php8.3-opcache php8.3-mbstring php8.3-xml php8.3-gd php8.3-curl
    ```
2.  **Configure Virtual Host**: Create `/etc/nginx/sites-available/wordpress`. Use the content from `settings.txt` (replace `SUBDOMAIN.DOMAIN.TLD` with your domain).
3.  **Enable Site**:
    ```bash
    sudo ln -s /etc/nginx/sites-available/wordpress /etc/nginx/sites-enabled/
    sudo rm /etc/nginx/sites-enabled/default
    sudo systemctl reload nginx
    ```

### WordPress
1.  **Download & Extract**:
    ```bash
    cd /tmp
    wget https://wordpress.org/latest.tar.gz
    tar -xzvf latest.tar.gz
    sudo rm -rf /var/www/html/*
    sudo cp -r wordpress/* /var/www/html/
    ```
2.  **Permissions**:
    ```bash
    sudo chown -R www-data:www-data /var/www/html
    ```
3.  **Configure**:
    ```bash
    sudo cp /var/www/html/wp-config-sample.php /var/www/html/wp-config.php
    sudo nano /var/www/html/wp-config.php
    # Update DB_NAME, DB_USER, and DB_PASSWORD with values from MySQL step.
    ```

## 5. Backup System

1.  **Install Python**: `sudo apt install python3`
2.  **Script Setup**:
    *   Copy `db_backup.py` to `/root/db_backup.py`.
    *   **Important**: Edit the script to ensure the backup path is valid:
        ```bash
        sudo nano /root/db_backup.py
        ```
        Change `BACKUP_FILE` to:
        ```python
        BACKUP_FILE: str = "/tmp/wordpress_backup.sql"
        ```
3.  **Cron Job**:
    *   Open the **root** crontab (ensures script runs with sudo privileges):
        ```bash
        sudo crontab -e
        ```
    *   Add the following line to run daily at midnight:
        ```cron
        0 0 * * * /usr/bin/python3 /root/db_backup.py
        ```
4.  **Log File**:
    ```bash
    sudo touch /var/log/backup.log
    sudo chmod 644 /var/log/backup.log
    ```
