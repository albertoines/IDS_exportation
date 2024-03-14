bash /home/pi/scripts/gitids.sh
cp -r /home/pi/IDS_exportation/zeek/*  /etc/suricata/rules/
cp -r /home/pi/IDS_exportation/zeek/* /usr/local/zeek/share/zeek/site/misp_zeek/
sudo systemctl restart suricata
sudo zeekctl deploy