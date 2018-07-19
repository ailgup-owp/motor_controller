cd /home/pi/motor_tester
while ! ping -c 1 -W 8.8.8.8; do
    echo "Waiting ..."
    sleep 1
done
git fetch --all
sudo chmod +x /home/pi/motor_tester/launch.sh
export DISPLAY=:0 ; python3 /home/pi/motor_tester/motor_test.py &
