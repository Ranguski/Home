#!/bin/bash

fileCount=$(ls | wc -l)
echo "Number of files - $fileCount"

for file in $(ls)
do
  echo $file
done

echo "Enter a value"
read userVal
echo "The user entered - $userVal"
