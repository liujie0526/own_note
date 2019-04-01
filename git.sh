
if [[ -z $1 ]]; then
cd /usr/local/nginx/html/note/own_note &&  git pull
exit 1
fi

git add $1 
git commit -m 'change by 13 ' 
git push origin master


