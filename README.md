# Getting Set Up for Developers
***
#### Kali Linux Installation
1. Install [kali linux image](https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/)
2. Install [7zip](https://www.7-zip.org/download.html)
2. unzip kali linux image in whatever directory you choose on your local machine.
 
#### Creating Kali Linux VM
1. Install [vmware workstation](https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html)
2. In the Vmware Workstation app:

   **a. File->Open**
   
   **b. Directory where Kali Linux Image is**
   
   
3. Edit the VM to have 4 GB of memory.
4. Power it on and select "I Copied it" when the notification pops up.
5. To log in to VM: 

   User: root ; pwd: toor

#### Setting up Developer environment after Opening Kali VM
1. Open terminal
2. Run the following commands in order to set up environment:

    a. `python3 -V ` (check that it is a Python version less than 3.7)
    
    b. `git clone <repository>`
    
    c. `pip3 install scapy`
    
    d. `pip3 install libnetfilter-queue-dev`
    
    e. `pip3 install netfilterqueue`

#### Run the following commands to start listening for Packets
1. On the same terminal
2. run: 

    a. `cd ntps/Capture`
    
    b. `python3 ProxyServer.py`
    
3. Open a new window terminal
4. run:

    `ping local`
    
