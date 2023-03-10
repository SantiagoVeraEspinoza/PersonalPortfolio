curl https://cryptingup.com/api/markets | jq -r '.markets |= sort_by(-.volume_24h) | .markets[0:10] | map("\(.symbol) \(.price)") | join("\n")'
