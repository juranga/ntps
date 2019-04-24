Set Up for Developers
***
#### Kali Linux Installation
1. Install [kali linux image](https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/)
2. Install [7zi[](https://www.7-zip.org/download.html)
2. unzip kali linux image on machine
 
#### Creating Kali Linux VM
1. Intall [vmware workstation](https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html)
2. In the Vmware Workstation app, open the kali linux image
3. Edit the VM to have 4 GB of memory.
4. Power it on, select "I Copied it"
5. User: root ; pwd: toor

#### Setting up Developer environment after Opening VMWare
1. Open terminal
2. Run the following commands in order to set up environment:
    `python3 -V ` (check that it is a Python version less than 3.7)
    `git clone <repository>`
    `pip3 install scapy`
    `pip3 install libnetfilter-queue-dev`
    `pip3 install netfilterqueue`

#### Run the following commands to start listening for Packets
1. Open terminal
2. run: 
    `cd ntps/Capture`

