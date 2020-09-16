content="
# Notes \n
"

for f in *.html **/*.html
do
  path="./$f"
  content="$content\n1. [$path]($path)  "
done

echo $content > README.md