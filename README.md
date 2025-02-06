# Keenetic Routing Creator

## Description
Application for creating a list of routes in the format Keenetic

## Networks

### All
https://gist.github.com/iamwildtuna/7772b7c84a11bf6e1385f23096a73a15

### Instagram
https://treeone.ru/diapazon-ip-adres-facebook-instagram-mikrotik/#comment-6910

### Get google IPs
```bash
curl https://www.gstatic.com/ipranges/goog.json | jq '.prefixes[].ipv4Prefix' | awk -F\" '{print $2}' | egrep -v "^$" | sort -V > google.txt
```
