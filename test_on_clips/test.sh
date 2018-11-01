#!/usr/bin/bash

let k=10  # Duration of clip
for i in {0..69}  # Number of clips, with 0-index
do
  python revised_measure_wav.py distu$i.wav  # Filename
  let l=$(((60/k)-1))
  if [ $i -gt $l ]
  then  
    let m=$(((i+1)/(60/k)))
    let s=$(((i+1)%(60/k)))
    echo "# @ $m min $((s*k)) - $(((s+1)*k)) seconds"
    echo "##################"
  else
    echo "# @ $((i*k)) - $(((i+1)*k)) seconds"
    echo "##################"
  fi
  sleep $k
done
