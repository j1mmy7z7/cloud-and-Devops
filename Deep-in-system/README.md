# Ansible Server Setup & WordPress Deployment

This project automates the provisioning of a secure Ubuntu server hosting a WordPress website, including network configuration, user management, security hardening, and a database backup strategy.

## Prerequisites

Before running this playbook, ensure your control node (the machine running Ansible) has the following installed:

*   **Ansible**: To execute the playbooks.
*   **Python 3**: Required by Ansible.
*   **Passlib**: A Python library used by Ansible to hash passwords for user creation.
    ```bash
    pip install passlib
    ```
*   **Ansible Collections**:
    *   `community.general`
    *   `community.mysql`
    *   `ansible.posix`
    *   `community.crypto`
    
    Install them using:
    ```bash
    ansible-galaxy collection install community.general community.mysql ansible.posix community.crypto
    ```

**Target Machine Requirements:**
*   A clean Ubuntu Server installation.
*   SSH access with a user having `sudo` privileges (default configured as `user` in variables).

## Project Structure

*   `playbook.yaml`: The main Ansible playbook containing all automation tasks.
*   `inventory.ini` / `inventory.yml`: Defines the target hosts.
*   `db_backup.py`: Python script for backing up the WordPress database.
*   `settings.txt`: Nginx configuration template for the WordPress site.
*   `secret.yml`: (Encrypted) Contains sensitive variables like passwords.

## Architecture & Implementation

### 1. Network Configuration
The playbook configures a **static IP address** using Netplan to ensure the server has a persistent network identity.
*   **Task**: `Configure Static IP and Verify Internet`
*   **Mechanism**: It generates a `/etc/netplan/50-cloud-init.yaml` file with the specified IP, gateway, and DNS servers, then applies the configuration.
*   **Verification**: Checks internet connectivity by pinging Google.

### 2. Security & Firewall
Security is a primary focus, implemented via UFW (Uncomplicated Firewall) and SSH hardening.
*   **Firewall (UFW)**: 
    *   Default policy is to **deny** incoming traffic.
    *   Allowed ports: `2222` (SSH), `80` (HTTP), `21` (FTP Control), and a passive FTP port range.
*   **SSH Hardening**:
    *   Port changed from default `22` to `2222`.
    *   Root login is **disabled**.
    *   Password authentication is disabled for the admin user (`luffy`), enforcing SSH key usage.

### 3. User Management
Three specific users are created with distinct roles:
*   **luffy**: Admin user.
    *   Access: SSH via **Public Key** only.
    *   Privileges: `sudo` access.
*   **zoro**: Standard user.
    *   Access: SSH via **Password**.
    *   Privileges: No `sudo` access.
*   **nami**: Backup user.
    *   Access: FTP only (restricted to `/backup`).
    *   Shell: `/usr/sbin/nologin` (cannot SSH).

### 4. Services Stack
The project deploys a LAMP-like stack (Linux, Nginx, MySQL, PHP).

*   **FTP (vsftpd)**: Configured for secure local user access, chrooted to home directories. Anonymous access is disabled.
*   **MySQL**: 
    *   Root remote login is disabled.
    *   Bound to `127.0.0.1` for local access only.
    *   A dedicated database and user are created for WordPress.
*   **Nginx & PHP**:
    *   Installs Nginx and PHP 8.3 (FPM and extensions).
    *   Configures a virtual host using `settings.txt` which restricts access to sensitive files like `wp-config.php`.
*   **WordPress**:
    *   Downloads and extracts the latest WordPress release.
    *   Configures `wp-config.php` automatically with the database credentials.

### 5. Backup System
A custom backup solution is implemented using Python and Cron.

*   **Script (`db_backup.py`)**:
    *   Executes `mysqldump` to export the WordPress database.
    *   Archives the SQL file into a `.tar` file with a timestamp.
    *   Logs the operation status to `/var/log/backup.log`.
    *   Files are stored in `/backup` (accessible to user `nami` via FTP).
*   **Automation (Cron)**:
    *   A cron job is scheduled to run the script daily.

## How to Run

1.  **Update Inventory**: Edit `inventory.ini` with your target server's IP address, you should consider user ther Inventory with the yml extensions which allows templating with dynamic variables.
2.  **Define Secrets**: Ensure you have the `secret.yml` file or define the necessary password variables (`luffy_password`, `zoro_password`, `nami_password`, `db_user_password`, `password` for root/ansible user).
3.  **Execute Playbook**:
    ```bash
    ansible-playbook -i inventory.ini playbook.yaml --ask-vault-pass --ask-pass
    ```
    *(Note: `--ask-vault-pass` is needed if you are using an encrypted `secret.yml`)*.
    *(Note: `--ask-pass` is also needed for the ssh connection )
  
4. if the use has not initial connetcion with ssh to the setup vm u can add this command to skip the initial ssh check
``` bash
'--ssh-extra-args="-o StrictHostKeyChecking=accept-new"'
``` or you can just connect with ssh first before running the playbook

## Troubleshooting

*   **SSH Connectivity**: If the playbook fails after changing the SSH port, verify that you are trying to connect on port `2222` for subsequent runs or manual checks.
*   **Netplan**: If the static IP configuration fails, ensure the interface name in the playbook matches the VM's actual interface (e.g., `eth0`, `ens3`).
