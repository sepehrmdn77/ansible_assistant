# 🚀 Ansible Assistant

**Ansible Assistant** is a powerful and intuitive GUI tool built in Python using [Flet](https://flet.dev/) to simplify and streamline Ansible operations across remote hosts.

---

## ✨ Features

- 🖥️ **Remote Host Detection**  
  Automatically fetches hosts from your SSH config (`~/.ssh/config`) for quick access.

- ⚙️ **One-click Software Installation**  
  Install popular tools like **Docker**, **PostgreSQL**, **MongoDB**, and **Node.js** with a single click using Ansible.

- 🔐 **SSH Key Authentication**  
  Secure access to your remote servers using your private key.

- 🌙 **Dark Mode UI**  
  Built with Flet — providing a sleek, responsive and modern interface.

---

## 📸 Screenshot

![App test](src/assets/App_test.png)

---

## 🛠️ Installation

### 🔹 Clone the Repo

```bash
git clone https://github.com/sepehrmdn77/ansible_assistant.git
cd ansible_assistant
```

### 🔹 Using Python

```bash
pip install -r requirements.txt
python src/main.py
```

### 🔹 Using Docker Compose

```bash
docker build -t ansible_assistant:latest .
docker compose up -d
```

---

## ✅ Requirements

- Python 3.8+
- Ansible
- Flet
- SSH-configured remote hosts
- Linux-based environment (recommended)

---

## ⚙️ Configuration

- Your `~/.ssh/config` file must be populated with remote host entries.
- The app reads the hostnames directly from this file and displays them in the GUI.

---

## 🧪 CI/CD Pipeline

This project includes a GitHub Actions workflow:

- ✅ Linting with **Flake8**
- 🚀 Auto-test on push and pull requests
- 🔐 Ensures code quality and stability

---

## 💡 Use Cases

- 🧑‍💻 DevOps engineers managing multiple servers
- 🛠️ System admins deploying essential services
- 👨‍🏫 Instructors teaching automation and Ansible basics

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repo
2. Create a branch: `git checkout -b new-feature`
3. Make your changes
4. Submit a pull request ✅

---

## 📬 Contact

📧 sepehrmaadani98@gmail.com  
🔗 [GitHub Profile](https://github.com/sepehrmdn77)

---

> Designed with ❤️ by [Sepehr Maadani](https://github.com/sepehrmdn77)
