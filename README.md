# Cloud and DevOps
This repository tracks my progress through various Cloud and DevOps projects. It uses Git Submodules to organize individual project implementations.

### Projects & Requirements
The links below point to the official project requirements and subject descriptions:

*   **Deep-in-net**: [Subject Details](https://github.com/01-edu/public/tree/master/subjects/devops/deep-in-net)
*   **Deep-in-system**: [Subject Details](https://github.com/01-edu/public/tree/master/subjects/devops/deep-in-system)
*   **CRUD Master**: [Subject Details](https://github.com/01-edu/public/tree/master/subjects/devops/crud-master-py)
*   **Play-with-containers**: [Subject Details](https://github.com/01-edu/public/tree/master/subjects/devops/play-with-containers)
*   **Orchestrator**: [Subject Details](https://github.com/01-edu/public/tree/master/subjects/devops/orcherstrator)
*   **cloud-design**: [Subjetc Details](https://github.com/01-edu/public/tree/master/subjects/devops/cloud-design)
*   **Code-Keeper**: [Subject Details](https://github.com/01-edu/public/tree/master/subjects/devops/code-keeper)
[!note] the cloud-desing project was done in azure is i had trouble making an aws account
---

### How to Clone
To clone this repository along with all project submodules:
```bash
git clone --recurse-submodules <repo-url>
```

### How to Update
If you have already cloned the repository and want to pull the latest changes for all submodules:
```bash
git pull --recurse-submodules
```
If you cloned without submodules and need to initialize them:
```bash
git submodule update --init --recursive
```
