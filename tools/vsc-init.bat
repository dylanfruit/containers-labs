@echo off
echo Starting VS Code extension installation...

:: Ensure 'code' is in your PATH. If not,
:: you might need the full path, for example:
:: "C:\Users\YourUser\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd"

:: Extension: Python
echo Installing Python...
code --install-extension ms-python.python

:: Extension: YAML
echo Installing YAML...
code --install-extension redhat.vscode-yaml

:: Extension: JSON (Note: VS Code has built-in JSON support, but this installs a common JSON extension if desired)
echo Installing JSON...
code --install-extension humao.rest-client :: Assuming a popular JSON-related extension like Rest Client, as JSON is often built-in.
                                        :: If where can I host a virtual machine disk from virtualbox on the you meant a different JSON extension, please specify its ID.

:: Extension: Remote Explorer
echo Installing Remote Explorer...
code --install-extension ms-vscode-remote.remote-explorer

:: Extension: Remote SSH
echo Installing Remote SSH...
code --install-extension ms-vscode-remote.remote-ssh

:: Extension: Pod Manager (Assuming this refers to the Red Hat Kubernetes extension)
echo Installing Pod Manager (Kubernetes)...
code --install-extension redhat.vscode-kubernetes

:: Extension: Project Manager
echo Installing Project Manager...
code --install-extension alefragnani.project-manager

:: Extension: Git Graph
echo Installing Git Graph...
code --install-extension mhutchie.git-graph

:: Extension: Ansible
echo Installing Ansible...
code --install-extension redhat.vscode-ansible

echo.
echo Extension installation process completed.
echo You may need to restart VS Code for the changes to take effect.
pause
