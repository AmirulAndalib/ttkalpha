while true
do
    sleep 1000 #sleep NUMBER[SUFFIX]. SUFFIX= seconds (s), minutes (m), hours (h) and days (d). Given value 60 is 60 sec
    echo "Preventing site from idling..."
    wget -q -O/dev/null $BASE_URL_OF_BOT
done
