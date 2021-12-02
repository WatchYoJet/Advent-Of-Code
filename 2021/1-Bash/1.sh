#!/bin/bash

part1() {
    last=0
    isBigger=-1
    cat input1.txt | grep -Eo '^[0-9]+' | while read -r line; do
        diff=$((line - last))
        if [ $diff -gt 0 ]; then
            ((isBigger=isBigger+1))
            echo "$isBigger"
        fi
        last=$line
    done | tail -1
}

part2() {
    mapfile nums < input1.txt
    last=0
    for i in {0..2}; do
        ((last=last+nums[i]))
    done
    isBigger=0
    counter=1
    curr=0
    while [ $counter -lt ${#nums[@]} ]; do
        ((curr=nums[counter]+nums[counter+1]+nums[counter+2]))
        if [ $curr -gt $last ]; then
            ((isBigger=isBigger+1))
        fi
        ((last=curr))
        ((counter=counter+1))
    done
    echo "$isBigger"
}

part1
part2