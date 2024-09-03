#!/bin/bash
sudo pip install cryptography plyer --break-system-packages


sudo mkdir -p /opt/wallet/wallet/keys
sudo mkdir -p /opt/wallet/requests


sudo chown -R root:root /opt/wallet/wallet
sudo find /opt/wallet/wallet -type d -exec chmod 700 {} +
sudo find /opt/wallet/wallet -type f -exec chmod 600 {} +


sudo chmod 777 /opt/wallet/requests


sudo cp wallet.py /opt/wallet/wallet/



echo "Write your username:"
read username







FILE_PATH="/opt/wallet/start_wallet.sh"
sudo echo -e "#!/bin/bash\n\ncd /opt/wallet/wallet\nsudo python3 wallet.py" > $FILE_PATH
sudo chmod +x $FILE_PATH
sudo chmod +x $FILE_PATH
sudo chown root:root $FILE_PATH

FILE_PATH="/opt/wallet/start_script_wallet.sh"
sudo echo -e "#!/bin/bash\n\ncd /opt/wallet\nsudo ./start_wallet.sh" > $FILE_PATH
sudo chmod +x $FILE_PATH
sudo chmod +x $FILE_PATH
sudo chown root:root $FILE_PATH




cp start_script_wallet.sh.desktop /home/${username}/.config/autostart/start_script_wallet.sh.desktop
echo "ALL ALL=(root) NOPASSWD: /opt/wallet/start_wallet.sh" | sudo EDITOR='tee -a' visudo


