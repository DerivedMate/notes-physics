echo "Updating README.md\n"
./create-readme.sh
git add -A
git commit -m"$1"
git push
