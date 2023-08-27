# AtlasOSInstallCheck
## A tool to check the integrity of the current Atlas OS installation

# How to get the script

## Cloning the repo (or download as ZIP)

Download the requirements with `pip install -r requirements.txt`, then proceed to the usage section (Python and pip are obviously required)

## Downloading a build from the releases page or the Github Actions

Extract and run.

# Usage:

Run the script with `run.cmd <path to Atlas Playbook (.apbx or extracted directory)> [-r] [-f] [-s] [-t] [-y]`

Parameters description :
- `-r` : Check registry entries
- `-f` : Check files
- `-s` : Check services
- `-t` : Check task scheduler entries
- `-y` : Skip confirmation prompts

If no parameters are specified, all checks will be run

### Please run the script with Admin privileges to avoid any permission errors (even so, some may occur)

Note: this tool is still under developpement so bugs may still be present. If you find some, please take the time to report them

## WARNING : This is not meant to apply the playbook ! Many essential steps are skipped ! Please use the standard means of installation !

# Support
This tool is meant to be used with the Atlas OS playbook, but should work with any other AME Wizard compatible playbooks. Use it at your own risk

### To request additional features, or report bugs, please open an issue on the GitHub repository


# Credit
Huge thanks to the AME and Atlas OS team for their amazing work to unbloat Windows and make it more private.
- [Atlas OS](https://atlasos.net/)
- [AME Wizard](https://ameliorated.io/)
- Credit to the Atlas OS team for the RunAsTI.cmd script
