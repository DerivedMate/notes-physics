echo "Updating README.md\n"
./create-readme.py "./" > README.md
git add -A
git commit -m"`date`"
git push
