#!/bin/bash
echo "Updating README.md\n"
./create-readme.py "./" > README.md
echo "Compile README, 'ma wait"
while [ true ] ; do
read -t 3 -n 1
if [ $? = 0 ] ; then break ;
else continue ;
fi
done

git add -A
git commit -m"`date`"
git push
