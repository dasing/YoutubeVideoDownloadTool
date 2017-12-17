#!/bin/bash
filename=$1
dstDir=$2
currDir=$(pwd)
slash='/'

mkdir -p $dstDir

exec < $filename

while read line
do	
	youtube-dl -f 'bestvideo[ext=mp4]/best[ext=mp4]/best' -o  "$currDir/$dstDir/%(title)s.%(ext)s" -- $line
done